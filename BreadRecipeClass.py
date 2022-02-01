#creating a class so I can import to other programs later (namely the discord bot I am working on), as opposed to the program for use when at desktop
class Recipe:

	def __init__(self, water, salt, yeast, sugar, oil, dough_amount):
		#multipled by 0.01 to convert to a percentage
		dough_amount = float(dough_amount)
		water_percentage = float(water) * 0.01

		salt_percentage = float(salt) * 0.01

		yeast_percentage = float(yeast) * 0.01

		sugar_percentage = float(sugar) * 0.01

		oil_percentage = float(oil) * 0.01

		total_percentage = (water_percentage + salt_percentage + yeast_percentage + sugar_percentage + oil_percentage)

		flour_amount = round(dough_amount / (1 + total_percentage))

		water_amount = round(water_percentage * flour_amount)

		salt_amount = round(salt_percentage * flour_amount)

		yeast_amount = round(yeast_percentage * flour_amount)

		sugar_amount = round(sugar_percentage * flour_amount)

		oil_amount = round(oil_percentage * flour_amount)

		self.water = water

		self.salt = salt

		self.yeast = yeast

		self.sugar = sugar

		self.oil = oil

		self.dough_amount = dough_amount

		self.recipe = f"Flour: {flour_amount} \nWater: {water_amount} \nSalt: {salt_amount} \nYeast: {yeast_amount} \nSugar: {sugar_amount}\nOil: {oil_amount}"

test = Recipe(70, 2, 2, 2, 2, 2000)
print(test.salt)