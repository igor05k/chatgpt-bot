import os
import openai
import config 
import json
import discord

# openai.api_key = os.getenv("OPENAI_API_KEY")
discord_bot_token = os.getenv("DISCORD_BOT_TOKEN")

# headers = {
#     "Authorization": f"Bearer {openai.api_key}"  
# }

# user_input = input("write any text so the bot can complete: ")

# capture event handler
# This example requires the 'message_content' intent.

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='$')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(token = discord_bot_token)


# class MyClient(discord.Client):
#     async def on_ready(self):
#         print(f'Logged on as {self.user}!')

#     async def on_message(self, message):
#         if message.content.startswith('$hello'):
#             await message.channel.send('Hello!')


# client = MyClient(intents=intents)
# client.run(discord_bot_token)




# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt=user_input,
#   max_tokens=50,
#   temperature=0,
#   headers=headers
# )

# convert to string so we can use json.loads
# convert_to_string = json.dumps(response)
# convert to python object
# json_response = json.loads(convert_to_string)

# iterate over the object and get the key
# result = json_response["choices"]

# for botResponse in result:
#     print(botResponse["text"])





