from discord import *
from discord.ext import commands
import requests
from BreadRecipeClass import *
from IDdictionary import *	
import json

#Setting the prefix that must be used before each command
client = commands.Bot(command_prefix = '!')

#When bot is ready to be used, Bot is active will be printed, and commands will be ready to be used.
@client.event
async def on_ready():
	print("Bot is active.")

#When run, he will repeat what you say as many times as you specify (default of 1).
@client.command()
async def say(ctx, word, times=1):
	if times > 10:
		await ctx.send("Sorry, that's too many! the limit is 10!")
	else:
		for x in range(times):
			await ctx.send(str(word))


#return recipe based on arguments given by user NEED TO RENAME TEST VARIABLES!!!!
@client.command()
async def recipe(ctx, *args):
	combined_arguments = ""
	for x in args:
		combined_arguments = combined_arguments + x
	removed_spaces = combined_arguments.replace(" ", "")
	argument_list = removed_spaces.split(',')
	final_recipe = Recipe(argument_list[0], argument_list[1], argument_list[2], argument_list[3], argument_list[4], argument_list[5])
	await ctx.send(str(final_recipe.recipe))



#Help Command, call the help command by itself for a list of commands to get help on, or with the command name for specific help on that command
help_list = {
"recipe" : "To use this command, call !recipe with 6 variables: hydration percentage, salt percentage, yeast percentage, sugar percentage, oil percentage, and the total amount of dough. Example '!recipe 60, 2, 0.4, 2, 2, 6000' would return a recipe of a total of 6000g of dough weight, 60 percent hydration, 2 percent salt, 0.4 percent yeast, 2 percent oil and sugar.",
"say" : "To use this command, simply call !say with the word you want to say, along with a second variable of the amount of times you want this word to be said. Example '!xsay hi 10' would result in the bot saying hi 10 times",
"gw2price" : "To use this command, call !gw2price with the name of the item you wish to check the buy and sell price of, e.g '!gw2sellprice twilight'",
}

@client.command()
async def helpcommand(ctx, command):
	await ctx.send(help_list[command.lower()])

@client.command()
async def commandslist(ctx):
	commands = ""
	for x in help_list.keys():
		commands = commands + x + ", "
	await ctx.send(commands)



#Function that gives the ID to any gw2 item from name (THIS WILL IDEALLY BE SWITCHED TO AN API SOLUTION, BUT NOTHING STRAIGHTFORWARD EXISTS FOR GW2 API ITEM NAME TO ITEM ID)
def get_ID_from_name(name):
	IDdictionary_keys = list(id_dictionary.keys())
	IDdictionary_values = list(id_dictionary.values())
	for y in IDdictionary_values:
		for x in y:
			if ((x[1].lower()).replace(" ", "")).replace("-", "") == ((name.lower()).replace(" ", "")).replace("-", ""):
				return(x[0])
			else:
				continue

def get_name_from_id(idnumber):
	IDdictionary_keys = list(id_dictionary.keys())
	IDdictionary_values = list(id_dictionary.values())
	for y in IDdictionary_values:
		for x in y:
			if x[0] == idnumber:
				return x[1]
			else:
				continue

@client.command()
async def gw2price(ctx,*args):
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
	print(copper_pieces)
	print(silver_pieces)
	print(gold_pieces)
	sellprice = f"{gold_pieces} gold pieces, {silver_pieces} silver pieces, and {copper_pieces} copper pieces"

	buyprice = str((x_dict["sells"]["unit_price"]))
	while len(buyprice) < 5:
		buyprice = "0" + buyprice
	copper_pieces = buyprice[-2:]
	silver_pieces = buyprice[-4:-2]
	gold_pieces = buyprice[0:-4]
	print(copper_pieces)
	print(silver_pieces)
	print(gold_pieces)
	buyprice = f"{gold_pieces} gold pieces, {silver_pieces} silver pieces, and {copper_pieces} copper pieces"
	await ctx.send(f"{get_name_from_id(idnumber)} currently sells for {sellprice} and buys for {buyprice}")	


client.run('NzA3MjY1MDUzOTEyNTk2NjQy.XrGTNA.OzqqScKKvafRma6gJAP9m45ehUQ')