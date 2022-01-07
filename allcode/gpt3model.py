import os
import pickle
import requests
import openai
import json 
from dotenv import load_dotenv, find_dotenv

load_dotenv("D:\\fixedJohnOliver\.env")

openai.api_key = os.getenv('OPENAITOKEN')
#uploadedfilejson = openai.File.create(file=open("nba_prepared.jsonl", encoding="utf8", errors="ignore"), purpose='fine-tune')

#finetunemodel = openai.FineTune.create(training_file=uploadedfilejson.get("id"), model = "davinci", n_epochs = 10)
#print(finetunemodel.get("id"))
#model_name = finetunemodel.get("id")


#OLD MODEL: print(openai.FineTune.retrieve(id="ft-ArN4t182xyNyyjlBF1UlkQ60"))
#OLD MODEL: openai api completions.create -m ada:ft-thegoats-2022-01-06-06-47-14 -p <YOUR_PROMPT>

#NEW MODEL openai api completions.create -m ada:ft-thegoats-2022-01-07-03-13-15 -p <YOUR_PROMPT>
#NEW MODEL 
prompt = "Stephen Curry"
print((prompt + openai.Completion.create(model="ada:ft-thegoats-2022-01-07-03-13-15", prompt=prompt, max_tokens=15).get("choices")[0].get("text").replace("->", "")))