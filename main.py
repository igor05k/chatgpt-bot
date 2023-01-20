import os
import openai
import config 
import json
import requests

openai.api_key = os.getenv("OPENAI_API_KEY")

headers = {
    "Authorization": f"Bearer {openai.api_key}"  
}

user_input = input("write any text so the bot can complete: ")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=user_input,
  max_tokens=17,
  temperature=0,
  headers=headers
)

# convert to string so we can use json.loads
convert_to_string = json.dumps(response)
# convert to python object
json_response = json.loads(convert_to_string)

# iterate over the object and get the key
result = json_response["choices"]

for botResponse in result:
    print(botResponse["text"])



