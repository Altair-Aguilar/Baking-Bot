#import libraries needed for discord, api, etc.
from discord import *
from discord.ext import commands
import requests
import json

#Import personal python scripts that were split off from this for easier readability. 
from BreadRecipeClass import *
from IDdictionary import *	
from scraper2 import *
from keys import *
from KingArthurSearchEngine import *


#Setting the prefix that must be used before each command
client = commands.Bot(command_prefix = '!')

#When bot is ready to be used, Bot is active will be printed, and commands will be ready to be used.
@client.event
async def on_ready():
	print("Bot is active.")


#Function that gives the ID to any gw2 item from name will be used for a command later(THIS WILL IDEALLY BE SWITCHED TO AN API SOLUTION, BUT NOTHING STRAIGHTFORWARD EXISTS FOR GW2 API ITEM NAME TO ITEM ID)
def get_ID_from_name(name):
	IDdictionary_keys = list(id_dictionary.keys())
	IDdictionary_values = list(id_dictionary.values())
	for y in IDdictionary_values:
		for x in y:
			if ((x[1].lower()).replace(" ", "")).replace("-", "") == ((name.lower()).replace(" ", "")).replace("-", ""):
				return(x[0])
			else:
				continue

#Function that does the reverse of the previous, instead getting the name from the ID Number, will be used for a command later
def get_name_from_id(idnumber):
	IDdictionary_keys = list(id_dictionary.keys())
	IDdictionary_values = list(id_dictionary.values())
	for y in IDdictionary_values:
		for x in y:
			if x[0] == idnumber:
				return x[1]
			else:
				continue



#Help Command, call the help command by itself for a list of commands to get help on, or with the command name for specific help on that command
help_list = {
"recipe" : "To use this command, call !recipe with 6 variables: hydration percentage, salt percentage, yeast percentage, sugar percentage, oil percentage, and the total amount of dough. Example '!recipe 60, 2, 0.4, 2, 2, 6000' would return a recipe of a total of 6000g of dough weight, 60 percent hydration, 2 percent salt, 0.4 percent yeast, 2 percent oil and sugar.",
"say" : "To use this command, simply call !say with the word you want to say, along with a second variable of the amount of times you want this word to be said. Example '!xsay hi 10' would result in the bot saying hi 10 times",
"gw2price" : "To use this command, call !gw2price with the name of the item you wish to check the buy and sell price of, e.g '!gw2sellprice twilight'",
"helpcommand" :'To use this command, call !helpcommand with any command name and it will return a message that explains what the command does.',
"commandslist" : "To use this command call !commandslist to get a list of all commands returned",
"help" : "To use this command, call !help to get a list of all commands returned",
"calendarday" : "To use this command, call !calendarday to get today's feast day returned",
"leetcode" : "To use this command, call !leetcode to get leetcode's daily challenge",
"kaf" : "To use this command, call !kaf with your search query and get the top result from King Arthur Flour's Site"
}

#Returns a help message for a certain command, taken from help_list
@client.command()
async def helpcommand(ctx, command):
	await ctx.send(help_list[command.lower()])


#lists all commands, two commands to allow !help to be used for the same result
@client.command()
async def commandslist(ctx):
	commands = ""
	for x in help_list.keys():
		commands = commands + x + ", "
	await ctx.send(commands)


@client.command()
async def help(ctx):
	commands = ""
	for x in help_list.keys():
		commands = commands + x + ", "
	await ctx.send(commands)



#When run, the bot will repeat what you say as many times as you specify (default of 1).
@client.command()
async def say(ctx, *args):
	words = ""
	for x in args:
		words = words + x + " "
	split_input = words.split(" ")
	split_input.pop(-1)
	if split_input[-1].isdigit() and int(split_input[-1]) < 11:
		times = split_input.pop(-1)
		times = int(times)
		repeat = ""
		for x in split_input:
			repeat = repeat + x + " "
		for x in range(times):
			await ctx.send(repeat)
	elif not split_input[-1].isdigit():
		repeat = ""
		for x in args:
			repeat = repeat + x + " "
		await ctx.send(repeat)
	else:
		await ctx.send("Sorry, the limit is 10!")


#return amounts for a bread recipe based on percentages given by the user
@client.command()
async def recipe(ctx, *args):
	combined_arguments = ""
	for x in args:
		combined_arguments = combined_arguments + x
	removed_spaces = combined_arguments.replace(" ", "")
	argument_list = removed_spaces.split(',')
	final_recipe = Recipe(argument_list[0], argument_list[1], argument_list[2], argument_list[3], argument_list[4], argument_list[5])
	await ctx.send(str(final_recipe.recipe))


#using the gw2 api and the previously created functions, determines the price of certain items in GW2 based on the user's input
@client.command()
async def gw2price(ctx,*args):
	try:
		name = ""
		for x in args:
			name = name + x
		idnumber = get_ID_from_name(name)
		x = requests.get(f"https://api.guildwars2.com/v2/commerce/prices/{idnumber}")
		x_dict = x.json()
		sellprice = str((x_dict["buys"]["unit_price"]))
		while len(sellprice) < 5:
			sellprice = "0" + sellprice
		copper_pieces = sellprice[-2:]
		silver_pieces = sellprice[-4:-2]
		gold_pieces = sellprice[0:-4]
		sellprice = f"{gold_pieces} gold pieces, {silver_pieces} silver pieces, and {copper_pieces} copper pieces"

		buyprice = str((x_dict["sells"]["unit_price"]))
		while len(buyprice) < 5:
			buyprice = "0" + buyprice
		copper_pieces = buyprice[-2:]
		silver_pieces = buyprice[-4:-2]
		gold_pieces = buyprice[0:-4]
		buyprice = f"{gold_pieces} gold pieces, {silver_pieces} silver pieces, and {copper_pieces} copper pieces"
		await ctx.send(f"{get_name_from_id(idnumber)} currently sells for {sellprice} and buys for {buyprice}")	
	except KeyError:
		await ctx.send("I think you spelled that wrong! Try again! Make sure you arent pluralizing an item that should not be.")



#takes the feast day from a calendar api and returns it to the user
@client.command()
async def calendarday(ctx):
	feasts_today = requests.get("http://calapi.inadiutorium.cz/api/v0/en/calendars/general-en/today")
	feasts_dict = feasts_today.json()
	feast = feasts_dict["celebrations"][0]["title"]
	await ctx.send(f"Today's Feast is {feast}")


#scrapes the leetcode website for the daily coding challenge and sends that result. (very slow right now as the bot has to fully load in the website to allow for dynamically-generated items to load in, need to run this code daily at the time that leetcode uploads their challenge and then cache the result for quick response.)
@client.command()
async def leetcode(ctx):
	await ctx.send(f"Todays Daily Leetcode Challenge Link: {get_link()}")


#Takes a query from the user and queries custom google search engine that only returns results from the King Arthur Baking Site, and sends that result to the user
@client.command()
async def kaf(ctx, query):
	await ctx.send(searchkaf(query))

#Runs the bot
client.run(bottoken)