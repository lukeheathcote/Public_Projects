#Tip Calculator
print("welcome to the tip calculator!" )
bill = float(input("What was the total bill? £"))
tip = int(input("How much tip would you like to give? "))
split = int(input("How many people would you like to split the bill? "))
#inputs done, Maths Next
bill_amount = bill / 100 * tip / split
totalbill = round(bill_amount, 2)
print(f"Each person should tip: {totalbill}")

