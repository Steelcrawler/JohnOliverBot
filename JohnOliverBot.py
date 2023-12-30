import os

import discord
from dotenv import load_dotenv
import pandas as pd
from People import People
import matplotlib.pyplot as plt

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
guild = "Steelcrawler's serverdasfasd"

client = discord.Client(intents=discord.Intents().all())

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    print(client.user.id)

nikhil = People('nikhil', {'blu', 'kane', 'nikhil', '<@!690756558698840157>'}, 690756558698840157)
akash = People('akash', {'akash', 'kash', 'asap', '<@!393251455685099521>'}, 393251455685099521)
adi = People('adi', {'adi', 'steel', 'steelcrawler', '<@!464402798235222027>'}, 464402798235222027)
anish = People('anish', {'swishy', 'anish', '<@!573361953649590274>'}, 573361953649590274)
aneesh = People('aneesh', {'rams', 'bloom', 'aneesh', 'bloomlmao', '<@!577675221352579095>'}, 577675221352579095)
akhil = People('akhil', {'boo', 'akhil', '<@!672615349786640385>', 'saboo'}, 672615349786640385)
edric = People('edric', {'edric', 'eddy', '<@!505598260451213363>'}, 505598260451213363)
satvik = People('satvik', {'cute', 'satvik', '<@!573359190962208768>'}, 573359190962208768)
vaibhav = People('vaibhav', {'vaibhav', 'vbev', 'bhav', '<@!550822418076270593>'}, 550822418076270593)

people_set = {nikhil, akash, adi, anish, aneesh, akhil, edric, satvik, vaibhav}

df = pd.DataFrame(columns=[people.name for people in people_set])

@client.event
async def on_message(message1):
    if '!history' == message1.content.lower():
        print('running history')
        names_dict = {'nikhil': nikhil.nicknames, 'akash': akash.nicknames, 
                      'anish': anish.nicknames, 'aneesh': aneesh.nicknames, 
                      'akhil': akhil.nicknames, 'edric': edric.nicknames, 
                      'satvik': satvik.nicknames, 'adi': adi.nicknames, 
                      'vaibhav': vaibhav.nicknames}
        
        counts_people = {people.name: {people.name: 0 for people in people_set} for people in people_set}
        total_counts_people = {people.name: 0 for people in people_set}
        
        async for message in message1.channel.history(limit=1000):
            message_author = None
            for people in people_set:
                if people.id == message.author.id:
                    message_author = people.name
            if message_author is not None:
                total_counts_people[message_author] += 1
                content_lower = message.content.lower()
                for name, name_list in names_dict.items():
                    if any(n in content_lower for n in name_list):
                        counts_people[message_author][name] += 1
        df = pd.DataFrame({name: {k: v / total_counts_people[name] * 100 if total_counts_people[name] != 0 else 0 
                                for k, v in counts.items()} 
                        for name, counts in counts_people.items()})
        print(df)
        df.plot(kind='bar', stacked=True)

        plt.title('Name Mentions by Person')
        plt.xlabel('Person')
        plt.ylabel('Percentage of Total Messages')
        plt.show()

        plt.show()
            
        # async for message in message1.channel.history(limit=1000000):
        #     if message.author.id == 464402798235222027:
        #         content_lower = message.content.lower()
        #         for name, name_list in names_dict.items():
        #             if any(n in content_lower for n in name_list):
        #                 counts[name] += 1



        # messages = [message1 async for message1 in message.channel.history() if message1.content.lower() != '!history']
        # for message1 in messages:
        #     print(message1.author)

    # if message.author.id in (541319380919910400, 724681050395115520):
    #     await message.add_reaction("\U0001F913") 

    # if  'im not' in message.content.lower():
    #     await message.channel.send("yes u are")
    
    # if message.author.id == 393251455685099521:
    #     await message.add_reaction("\U0001F5FA")

client.run(token)