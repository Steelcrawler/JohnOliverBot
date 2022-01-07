consumer_key = "MpM1ALIsBtZb0iQtbLiFyoHMz"
consumer_secret = "cUnNC3vXj8erKQ0Vo900CnNnhj9FW95aPX3xvXtgZZsgSsuP03"
access_token = "1098331938006290432-IDgC0W39hf16f28ExmvxL1mSUCODwt"
access_token_secret = "Ou2mN8M0GFFajIOPdeBsV0EXKddiXomLaFwhx5sqfn7S1"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAADLXgEAAAAAUhe62zaVp6Ky%2FgQrUZ79%2FTPaHp8%3DwwEHRtXBJviv9dJuD4cxyWAigPQHAxokMTBM0PTqVL4MsitzS1"
import tweepy
import json
import jsonlines
import re
client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

userShams = "ShamsCharania"
#shams = 
filename = 'nbanews.json'
lst = []
dataShams, _, _, _, = client.get_user(username=userShams)
ShamsID = dataShams.get("id")
userWoj = "wojespn"
dataWoj, _, _, _, = client.get_user(username=userWoj)
WojID = dataWoj.get("id")
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

    
'''

        
    
