import os
import openai
import config 
import json
import discord
from discord.ext import commands

openai.api_key = os.getenv("OPENAI_API_KEY")
discord_bot_token = os.getenv("DISCORD_BOT_TOKEN")

headers = {
    "Authorization": f"Bearer {openai.api_key}"  
}

def fetchResponse(input):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=input,
        max_tokens=50,
        temperature=0,
        headers=headers
    )

    # convert to string so we can use json.loads
    convert_to_string = json.dumps(response)

    # convert to python object (deserialize it)
    json_response = json.loads(convert_to_string)

    # iterate over the object and get the key
    result = json_response["choices"]

    for botResponse in result:
        return botResponse["text"]


# start bot setup
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='$')

@bot.event
async def on_message(userInput):
    if userInput.author == bot.user:
        return
        
    response = fetchResponse(userInput.content)
    await userInput.channel.send(response)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(token = discord_bot_token)
