from twython import Twython
import pandas as pd
import json
import os
import sys

def get_authorization():
    return Twython(consumer_key, consumer_secret, access_token, access_secret)
def get_my_credentials(tweets):
    return tweets.verify_credentials()
# for security, we can load credentials from json file or sys
# before this step, you should use key.py to generate your json file

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_secret = os.getenv('ACCESS_TOKEN_SECRET')


# Instantiate an object
tweets = get_authorization()
credential = get_my_credentials(tweets)

print(credential)
# Create a query:    q, result_type, count and lang
# respectively for the search keyword, type, count, and language of results.
query = {
        'q': 'Boston celtics',  # search keyword
        'result_type': 'popular',  # search type
        'count': 100,   # count
        'lang': 'en', # languages of results
        }

# Search tweets for query's information
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

with open("twitter_info.json", "w") as file:
    json.dump(dict_, file,indent=4)
with open("my_credentials_info.json", "w") as file:
    json.dump(credential, file,indent=4)

print(dict_)
