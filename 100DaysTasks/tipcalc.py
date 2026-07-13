print("Welcome to Tip Calculator!")
cost = float(input("How much did the meal cost you? "))
tip = int(input("What percentage are you planning to give the staff as a tip? "))
people = int(input("How many people are there behind the table? "))
tipPercentage = cost / 100 * tip
costAfterTip = tipPercentage + cost
costPerPerson = costAfterTip / people
print("You should pay " + str(costPerPerson))

#polished approach
final = (((cost / 100) * tip)+cost)/people
print("You should pay " + str(final))