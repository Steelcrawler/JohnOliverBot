import pandas as pd
import requests
import praw 
import os
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv("D:\\fixedJohnOliver\.env")
reddit = praw.Reddit(
    client_id=os.getenv("REDDITCLIENTID"),
    client_secret=os.getenv("REDDITCLIENTSECRET"),
    user_agent=os.getenv("REDDITUSERAGENT"),
    username=os.getenv("REDDITUSERNAME"),
    password=os.getenv("REDDITPASSWORD"),
)

df = pd.DataFrame(columns = ['text', 'response'])



for submission in reddit.subreddit("askreddit").top(limit=500):
    submission.comments_sort = "top"
    top_comment = list(submission.comments)
    for i in range(3):
        top_response =  top_comment[i].body
        df = df.append({'text': str(submission.title), 'response': top_response}, ignore_index=True)

df.to_pickle("top500responses.pkl") 
#df.head()

#Directory: D:\RedditTextDatabase
#df = pd.read_pickle("top100responses.pkl")
#df.head()
#save_path = "D:\RedditTextDatabase" 
#text_end = ".txt"
##completeDirectory = save_path + "\\" "final" + text_end
#f = open(completeDirectory, "w+",  encoding = "utf-8")
#for i in range(0, len(df), 1):
    #f.write(df['text'].values[i] + " " + df['response'].values[i] + "\n")
#f.close()

filename = 'testing.json'
lst = []
# Append the new dict to the list and overwrite whole file
with open(filename, mode='w+') as f:
    for i in range(0, len(df), 1):
        lst.append({"text": df['response'].values[i]})
    json.dump(lst, f)
        

