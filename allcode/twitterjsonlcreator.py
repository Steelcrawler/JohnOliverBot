import tweepy
import json
import jsonlines
import re
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv("D:\\fixedJohnOliver\.env")
client = tweepy.Client(os.getenv("TWITTERBEARER_TOKEN"), os.getenv("TWITTERCONSUMER_KEY"), os.getenv("TWITTERCOSUMER_SECRET"), os.getenv("TWITTERACCESS_TOKEN"), os.getenv("TWITTERACCESS_TOKEN_SECRET"))

userShams = "ShamsCharania"
#shams = 
filename = 'nbanews.json'
lst = []
dataShams, _, _, _, = client.get_user(username=userShams)
ShamsID = dataShams.get("id")
userWoj = "wojespn"
dataWoj, _, _, _, = client.get_user(username=userWoj)
WojID = dataWoj.get("id")
print(WojID)
'''
with jsonlines.open('nba.jsonl', mode='a') as writer:

    tweetsShams = client.get_users_tweets(id=ShamsID, max_results=5)
    current_id = tweetsShams[3].get("newest_id")
    for i in range(32):
        tweetsShams = client.get_users_tweets(id=ShamsID, max_results=100, until_id = current_id)
        current_id = tweetsShams[3].get("oldest_id")

        for j in range(len(tweetsShams[0])):
            text = str(tweetsShams[0][j])
            URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
            cleaned_string = URLless_string.replace("\n", "")
            fifth_space = cleaned_string.find(" ")
            for k in range(0, 5, 1):
                fifth_space = cleaned_string.find(" ", fifth_space+k)
            completion_start = fifth_space+1
            writer.write({"prompt": cleaned_string[:fifth_space], "completion": cleaned_string[completion_start:]})

    tweetsWoj = client.get_users_tweets(id=WojID, max_results=5)
    current_id = tweetsWoj[3].get("newest_id")
    for i in range(32):
        tweetsWoj = client.get_users_tweets(id=WojID, max_results=100, until_id = current_id)
        current_id = tweetsWoj[3].get("oldest_id")

        for j in range(len(tweetsWoj[0])):
            text = str(tweetsWoj[0][j])
            URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
            cleaned_string = URLless_string.replace("\n", "")
            fifth_space = cleaned_string.find(" ")
            for k in range(0, 5, 1):
                fifth_space = cleaned_string.find(" ", fifth_space+k)
            completion_start = fifth_space+1
            writer.write({"prompt": cleaned_string[:fifth_space], "completion": cleaned_string[completion_start:]})
    
    #writer.write_all(lst)
    #json.dump(lst, f)
'''


        
    
