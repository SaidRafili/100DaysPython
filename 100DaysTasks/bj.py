import random

#simple version
firstCard = random.randint(1,21)
secondCard = random.randint(1,21)
card = random.randint(1,21)
compHand = random.randint(1,21)
total = firstCard + secondCard

print("Welcome to BlackJack Table")
print("Your hand is " + str(firstCard) + " " + str(secondCard))
print("Comp hand is " + str(compHand))
addedCards = input("Do you want to add card (yes/no) ? ")


if addedCards == "yes":
    total = firstCard + secondCard + card
elif addedCards == 'no':
    total = firstCard+ secondCard
else:
    print("Invalid input. Please submit yes or no")

print(total)

if total > compHand and total < 21:
    print("You win")
elif total < compHand or total > 21:
    print("You lose")
else:
    print("Error result")
