# Import libraries
# pip install twython
# pip install google.cloud
# import pandas to save data
from google.cloud import language
from twython import Twython
import pandas as pd
import json
import re

# for security, we can load credentials from json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'], creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])

# get an autherization
# before this step, you should set GOOGLE_APPLICATION_CREDENTIALS 
# in linux/mac , it should be "export GOOGLE_APPLICATION_CREDENTIALS='file Path' " 
client = language.LanguageServiceClient()


# Search tweets containing the key word
tweet_list = []
for status in tweets.search(q='NBA',count=300)['statuses']:
    tweet_list.append(status['text'])

df  = pd.DataFrame(tweet_list)
#remove duplicates from list
df.drop_duplicates(inplace = True)
df['text'] = df[0]

# create a new dataframe which can use to modify the text
tl_list = pd.DataFrame(df)
print(tl_list[0])
tl_list["text"] = tl_list[0]
#print(tl_list['text'])

# switch uppercase to lowercase and remove other special letter 
remove = lambda x: re.sub('RT @\w+: '," ",x)
rt = lambda x: re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",x)
tl_list["text"] = df.text.map(remove).map(rt)
tl_list["text"] = df.text.str.lower()

#print(tl_list)
#print(tl_list.head(5))
  
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
#print(tl_list)

