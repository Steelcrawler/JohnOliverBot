global creamStocksMarketCap 
global creamStockSharesAvailable 
global creamStockValue

import os

import discord
import pickle
from dotenv import load_dotenv, find_dotenv

load_dotenv("D:\\fixedJohnOliver\.env")

token = os.getenv("DISCORDTOKEN")
guild = "Steelcrawler's serverdasfasd"git

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    print(client.user.id)

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        'leave.'
    )

@client.event
async def on_message(message):
    if message.author.id in (541319380919910400, 724681050395115520):
        await message.add_reaction("\U0001F913") 

    if  'im not' in message.content.lower():
        await message.channel.send("yes u are")
    
    if message.author.id == 393251455685099521:
        await message.add_reaction("\U0001F5FA")