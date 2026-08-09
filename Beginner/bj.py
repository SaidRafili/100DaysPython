import random

#simple version
firstCard = random.randint(1,11)
secondCard = random.randint(1,11)
card = random.randint(1,11)
compHand = random.randint(1,11)
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

#using def
def playingBlackJack():

    def firstHand(cards):
        shuffled = random.choice(cards)
        return shuffled
    
    def keepPlaying():
        playerSum = sum(playerCards)
        compSum = sum(compCards)
        if playerSum > 21:
            print("You lost, your cards are busted")
        elif playerSum < 21 and compSum > playerSum:
            print("You lost, opponent's hand is greater than yours")
        elif playerSum < 21 and compSum == playerSum:
            print("Draw, both hands are equal")
        elif playerSum < 21 and compSum < playerSum:
            print("You won.")

    
    cards = [1,2,3,4,5,6,7,8,9,10,11,10,10,9,8,10,7,6]
    playerCards = []
    compCards = []
    playerCards.append(firstHand(cards))
    playerCards.append(firstHand(cards))
    compCards.append(firstHand(cards))
    print(f"Your hands: {playerCards} ")
    print(f"Opponent's hand: {compCards}") 
    hit = input("Do you want to get cards from deck? (y/n) ")
    if hit == "y":
        playerCards.append(firstHand(cards))
        print(f"Your new hand: {playerCards}")
        keepPlaying()
    elif hit == "n":
        keepPlaying()

        
playingBlackJack()
