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


#return recipe based on arguments given by user NEED TO RENAME TEST VARIABLES!!!!
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



#Help Command, call the help command by itself for a list of commands to get help on, or with the command name for specific help on that command
help_list = {"recipe" : "To use this command, call .recipe with 6 variables: hydration percentage, salt percentage, yeast percentage, sugar percentage, oil percentage, and the total amount of dough."}

@client.command()
async def helpcommand(ctx, command):
	await ctx.send(help_list[command.lower()])

client.run('NzA3MjY1MDUzOTEyNTk2NjQy.XrGTNA.OzqqScKKvafRma6gJAP9m45ehUQ')