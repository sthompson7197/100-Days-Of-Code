#This Tip Calculator calculates the total amount each person in a party would have to pay, plus tip.

print("Welcome to the tip calculator!")
totalBill = input("What was the total bill?")
tipPercentage = input("How much tip would you like to give? 10, 12, or 15?")
peopleCount = input("How many people to split the bill?")



totalBill_as_float = float(totalBill)
tipPercentage_as_float = float(tipPercentage)
peopleCount_as_int = int(peopleCount)

amountPerson = ((totalBill_as_float * (tipPercentage_as_float/100)) / peopleCount_as_int) + (totalBill_as_float/peopleCount_as_int)


print(f"Each person should pay: ${amountPerson:.2f}")