import requests
import asyncpraw 
import pandas as pd
import openai
import asyncio
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv("D:\\fixedJohnOliver\.env")
# set pandas viewing options
pd.set_option("display.max_columns", None)
pd.set_option('display.width', None)
pd.set_option("max_colwidth", None)
#pd.reset_option("max_colwidth")

reddit = asyncpraw.Reddit(
    client_id=os.getenv("REDDITCLIENTID"),
    client_secret=os.getenv("REDDITCLIENTSECRET"),
    user_agent=os.getenv("REDDITUSERAGENT"),
    username=os.getenv("REDDITUSERNAME"),
    password=os.getenv("REDDITPASSWORD"),
)   

df = pd.DataFrame(columns = ['text', 'response'])

async def getdata(df):     
    subreddit = await reddit.subreddit("askreddit") #subreddit object
    async for submission in subreddit.top(): #iterates throught ListingGenerator return through subreddit.top
        submission.comments_sort = "top"
        top_comment = submission.comments() #gets 3 top comments from submission
        for i in range(3):
            top_response =  top_comment[i].body
            df = df.append({'text': str(submission.selftext), 'response': top_response}, ignore_index=True)


session.close()
