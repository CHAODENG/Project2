from twython import Twython
import pandas as pd
import json

def get_authorization(creds):
    return Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'],creds['ACCESS_TOKEN'],creds['ACCESS_SECRET'])
def get_my_credentials(tweets):
    return tweets.verify_credentials()
# for security, we can load credentials from json file
# before this step, you should use key.py to generate your json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
tweets = get_authorization(creds)
credential = get_my_credentials(tweets)
print(tweets.get_home_timeline())

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
