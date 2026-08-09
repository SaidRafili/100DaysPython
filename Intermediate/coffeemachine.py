menu = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":20,
        },
        "cost":3.0,
    },
    "latte": {
        "ingredients":{
            "water":150,
            "coffee":50,
            "milk":100,
        },
        "cost":6.0,
    },
    "americano":{
        "ingredients":{
            "water":200,
            "coffee":100,
        },
        "cost":5.0,
    },
}

resources = {
    "water":300,
    "milk":150,
    "coffee":150,
}

def report():
    print(f"Current measure of water: {resources["water"]}")
    print(f"Current measure of milk: {resources["milk"]}")
    print(f"Current amount of coffee: {resources['coffee']}")

def payment():
    coffeType = input("Chose the type of coffee you prefer to drink! Espresso, Latte, Americano \n").lower()
    for i in range(100):
        if coffeType not in menu:
            coffeType = input("Wrong order, look up to the menu and make your choice again! Espresso, Latte, Americano \n")
        else:
            break
    coffeeValue = menu[coffeType].get("cost")

    beshQepik = int(input("How many 5 Cents will you insert? \n"))
    onQepik = int(input("How many 10 Cents will you insert? \n"))
    iyirmiQepik = int(input("How many 20 Cents will you insert? \n"))
    elliQepik = int(input("How many 50 Cents will you insert? \n"))
    Manat = int(input("How many Dollars will you insert? \n"))

    beshQepikValue = beshQepik * 5
    onQepikValue = onQepik * 10
    iyirmiQepikValue = iyirmiQepik * 20
    elliQepikValue = elliQepik * 50
    ManatValue = Manat * 100

    totalValue = (beshQepikValue + onQepikValue + iyirmiQepikValue + elliQepikValue + ManatValue) / 100
    if totalValue == coffeeValue:
        print("Success")
    elif totalValue > coffeeValue:
        change = totalValue - coffeeValue
        print(f"Your coffee is prepared, here is your change {change:,.2f}")
    elif totalValue < coffeeValue:
        print("Your payment is not enough") 
    else:
        pass

    def resourceUsage():
        nonlocal coffeType
        waterToBeUsed = menu.get(coffeType).get("ingredients").get("water")
        milkToBeUsed = menu.get(coffeType).get("ingredients").get("milk")
        coffeeToBeUsed = menu.get(coffeType).get("ingredients").get("coffee")
        resources["water"] -= waterToBeUsed
        resources["milk"] -= milkToBeUsed
        resources["coffee"] -= coffeeToBeUsed
        report()

    resourceUsage()
payment()