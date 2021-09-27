# Import libraries
# pip install twython
# import pandas to save data
from twython import Twython
import pandas as pd
import json

# for security, we can load credentials from json file
# before this step, you should use key.py to generate your json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Create a query:    q, result_type, count and lang
# respectively for the search keyword, type, count, and language of results.
query = {'q': 'Boston celtics',  # search keyword
        'result_type': 'popular',  # search type
        'count': 30,   # count
        'lang': 'en', # languages of results
        }

# Search tweets for query's information
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# save data in a pandas DataFrame 
# it can be easier to  manipulate
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)
print(df)
