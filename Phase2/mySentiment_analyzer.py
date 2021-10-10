# Import libraries
# pip install twython, Flask, google.cloud
# import pandas to save data
from google.cloud import language
from twython import Twython
from flask import Flask
from flask import render_template
from flask import request
import requests
import pandas as pd
import json
import re

app = Flask(__name__)
# the content of the front page
@app.route('/')
def search_page():
   return render_template('search.html')


#Search with key words and return relevent content from Twitter
@app.route('/search', methods = ['GET', 'POST'])
def search():
    keyword = request.form.get('wd')
    def retrieve_Data(keyword):
        tweet_list = []
        #Count_values for sentiment
        with open("twitter_credentials.json", "r") as file:
            creds = json.load(file)
        # Instantiate an object
        tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'], creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])

        for status in tweets.search(q = keyword,count=100)['statuses']:
            tweet_list.append(status['text'])
        return tweet_list
    tweet_list = retrieve_Data(keyword)

    df = pd.DataFrame(tweet_list)
    
    #remove duplicates from list
    df.drop_duplicates(inplace = True)
    df['text'] = df[0]
    # create a new dataframe which can use to modify the text
    tl_list = pd.DataFrame(df)
    tl_list["text"] = tl_list[0]

    # switch uppercase to lowercase and remove other special letter 
    remove = lambda x: re.sub('RT @\w+: '," ",x)
    rt = lambda x: re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",x)
    tl_list["text"] = df.text.map(remove).map(rt)
    tl_list["text"] = df.text.str.lower()
    # do sentiment analysis
    sentiment_analysis(tl_list)
    # output the count and percentage for each type of sentiments
    total_count = count_percentage(tl_list,"sentiment")
    print(total_count) 
    
    # export the json file which makes users look at feedback or recommendation clearer.
    with open('feedback_list.json', 'w') as fout:
        json.dump(tweet_list, fout, indent = 6)  
    recommendation_dic = {}
    for index in range(len(tweet_list)):
        recommendation_dic[index] = tweet_list[index]
    return json.dumps(recommendation_dic,indent=6)
    
#print(tl_list.head(5))
def sentiment_analysis(tl_list):
    # get an autherization
    # before this step, you should set GOOGLE_APPLICATION_CREDENTIALS 
    # in linux/mac , it should be "export GOOGLE_APPLICATION_CREDENTIALS='file Path' " 
    client = language.LanguageServiceClient()
    for index,text in tl_list['text'].iteritems():
        document = language.Document(content=text.encode('utf-8'), type_=language.Document.Type.PLAIN_TEXT)

        sentiment = client.analyze_sentiment(document=document).document_sentiment

        
        tl_list.loc[index,'score'] = sentiment.score
        if sentiment.score >= -1.0 and sentiment.score < -0.5:
            tl_list.loc[index, 'sentiment'] = "Clearly Negative"
        elif sentiment.score > 0.5 and sentiment.score <= 1:
            tl_list.loc[index, 'sentiment'] = "Clearly Positive"
        elif sentiment.score >= -0.1 and sentiment.score <= 0.1: 
            tl_list.loc[index, 'sentiment'] = "Neutral"
        else:
            tl_list.loc[index, 'sentiment'] = "Mixed";

def count_percentage(twitter_list,column):
    total=twitter_list.loc[:,column].value_counts(dropna=False)
    percentage=round(twitter_list.loc[:,column].value_counts(dropna=False,normalize=True)*100,2)
    return pd.concat([total,percentage],axis=1,keys=['Total','Percentage'])

if __name__ == '__main__':
    app.run(debug = True)
