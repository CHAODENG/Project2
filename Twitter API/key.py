import json

# First, entering your keys/secrets as strings in the following fields
credentials = {}
credentials['CONSUMER_KEY'] = 'Enter your consumer key' 
credentials['CONSUMER_SECRET'] = 'Enter your consumer secret' 
credentials['ACCESS_TOKEN'] = 'Enter your access token'   
credentials['ACCESS_SECRET'] = 'Enter your access secret' 

# Saving the credentials object to json file
with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)
