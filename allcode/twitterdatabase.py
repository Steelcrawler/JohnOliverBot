import tweepy
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv("D:\\fixedJohnOliver\.env")
client = tweepy.Client(os.getenv("TWITTERBEARER_TOKEN"), os.getenv("TWITTERCONSUMER_KEY"), os.getenv("TWITTERCOSUMER_SECRET"), os.getenv("TWITTERACCESS_TOKEN"), os.getenv("TWITTERACCESS_TOKEN_SECRET"))

userShams = "ShamsCharania"
#shams = 
filename = 'nbanews.json'
lst = []
data, _, _, _, = client.get_user(username=userShams)
ShamsID = data.get("id")

with open(filename, mode='w+') as f:
    tweets = client.get_users_tweets(id=ShamsID, max_results=5)
    current_id = tweets[3].get("newest_id")
    for i in range(30):
        tweets = client.get_users_tweets(id=ShamsID, max_results=100, until_id = current_id)
        current_id = tweets[3].get("oldest_id")
        for j in range(len(tweets[0])):
            text = str(tweets[0][j])
            fifth_space = text.find(" ")
            for k in range(0, 5, 1):
                fifth_space = text.find(" ", fifth_space+k)
            completion_start = fifth_space+1
            lst.append({"prompt": text[:fifth_space], "completion": text[completion_start:]})
    json.dump(lst, f)
'''

    
'''

        
    
