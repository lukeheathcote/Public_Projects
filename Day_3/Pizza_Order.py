print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

pepperoni_price = 0
extra_cheese_price = 0
size_price = 0
if size == "S" or size == "s":
    size_price =  15
elif size == "M" or size == "m":
    size_price =  20
elif size == "L" or size == "l":
    size_price = 25

if pepperoni == "Y" or pepperoni == "y":
    pepperoni_price = 2
else:
    pepperoni_price = 0

if extra_cheese == "Y" or extra_cheese == "y":
    extra_cheese_price = 1

new_cost = size_price + pepperoni_price + extra_cheese_price

print(f"Your final bill is: $ {new_cost}")

