from discord import *
from discord.ext import commands
import requests
from BreadRecipeClass import *

#Setting the prefix that must be used before each command
client = commands.Bot(command_prefix = '!')

#When bot is ready to be used, Bot is active will be printed, and commands will be ready to be used.
@client.event
async def on_ready():
	print("Bot is active.")

#When run, he will repeat what you say as many times as you specify (default of 1).
@client.command()
async def say(ctx, word, times=1):
	for x in range(times):
		await ctx.send(str(word))
#return recipe based on arguments given by user
@client.command()
async def recipe(ctx, *args):
	x = ""
	for y in args:
		x = x + y
	print(x)
	argues = x.replace(" ", "")
	print(argues)
	argus = argues.split(',')
	print(argus)
	send = Recipe(argus[0], argus[1], argus[2], argus[3], argus[4], argus[5])
	await ctx.send(str(send.recipe))

client.run('NzA3MjY1MDUzOTEyNTk2NjQy.XrGTNA.OzqqScKKvafRma6gJAP9m45ehUQ')