consumer_key = "MpM1ALIsBtZb0iQtbLiFyoHMz"
consumer_secret = "cUnNC3vXj8erKQ0Vo900CnNnhj9FW95aPX3xvXtgZZsgSsuP03"
access_token = "1098331938006290432-IDgC0W39hf16f28ExmvxL1mSUCODwt"
access_token_secret = "Ou2mN8M0GFFajIOPdeBsV0EXKddiXomLaFwhx5sqfn7S1"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAADLXgEAAAAAUhe62zaVp6Ky%2FgQrUZ79%2FTPaHp8%3DwwEHRtXBJviv9dJuD4cxyWAigPQHAxokMTBM0PTqVL4MsitzS1"
import tweepy
import json
client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

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

        
    
