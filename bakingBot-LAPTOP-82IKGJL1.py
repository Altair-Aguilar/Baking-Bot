from discord import *
from discord.ext import commands
import requests
from calculator import *

#Setting the prefix that must be used before each command
client = commands.Bot(command_prefix = '!')

#Messing around with APIS
x = requests.get("https://api.spoonacular.com/recipes/complexSearch?apiKey=e5982d8adff44262a8d0ad42b5bf9d4c")
print(x.status_code)
print(x.text)
#When bot is ready to be used, Bot is active will be printed, and commands will be ready to be used.
@client.event
async def on_ready():
	print("Bot is active.")

#When run, he will repeat what you say as many times as you specify (default of 1).
@client.command()
async def say(ctx, word, times=1):
	for x in range(times):
		await ctx.send(str(word))

client.run('NzA3MjY1MDUzOTEyNTk2NjQy.XrGTNA.OzqqScKKvafRma6gJAP9m45ehUQ')