import requests
import asyncpraw 
import pandas as pd
import openai
import asyncio

# set pandas viewing options
pd.set_option("display.max_columns", None)
pd.set_option('display.width', None)
pd.set_option("max_colwidth", None)
#pd.reset_option("max_colwidth")

reddit = asyncpraw.Reddit(
    client_id="mCsA5jOs0TOgWdVYnYm93g",
    client_secret="Wl7wE88pqGP1q_kWtRHci5Rr380zWQ",
    user_agent="web:JohnOliverBot:0.0.1 (by /u/_Steelcrawlwr)",
    username="_Steelcrawlwr",
    password="NSIRC123",
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
