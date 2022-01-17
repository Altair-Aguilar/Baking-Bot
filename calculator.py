#Gives amounts of flour, salt, yeast, etc. for a specified amount of dough at a specified percent of the flour

#Asks user for percentages

flour_percentage = 100

water_percentage = float(input("What percent hydration will this be?")) * 0.01

salt_percentage = float(input("What percent salt will this be?")) * 0.01

yeast_percentage = float(input("What percent yeast will this be?")) * 0.01

sugar_percentage = float(input("What percent sugar will this be?")) * 0.01

oil_percentage = float(input("What percent oil will this be?")) * 0.01

dough_amount = float(input('How many grams of dough do you want to make?'))

total_percentage = (water_percentage + salt_percentage + yeast_percentage + sugar_percentage + oil_percentage)

#Figures out amounts for each ingredient from percentages
flour_amount = round(dough_amount / (1 + total_percentage))

water_amount = round(water_percentage * flour_amount)

salt_amount = round(salt_percentage * flour_amount)

yeast_amount = round(yeast_percentage * flour_amount)

sugar_amount = round(sugar_percentage * flour_amount)

oil_amount = round(oil_percentage * flour_amount)

#Displays the amounts to the console
print(f"Flour: {flour_amount} \nWater: {water_amount} \nSalt: {salt_amount} \nYeast: {yeast_amount} \nSugar: {sugar_amount}\nOil: {oil_amount}")
x = input("To exit, close the program or press any key and then enter")
