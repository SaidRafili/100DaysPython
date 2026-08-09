import random
from art import *
art = text2art("Guess The Number")
print(art)
def guessNumber():
    numberToBeGuessed = random.randint(1,100)
    difficulty = input("Choose difficulty: easy/hard \n")
    numberByUser = int(input("Guess the number the cpu has decided: \n"))
    guesses = ""
    if difficulty == "easy":
        guesses = 10
        for i in range(guesses):
            if numberByUser == numberToBeGuessed:
                print("Success")
            else:
                guesses -= 1
                print(f"You have {guesses} left")
                numberByUser = int(input("Guess the number the cpu has decided: \n"))
    elif difficulty == "hard":
        guesses = 5
        for i in range(guesses):
            if numberByUser == numberToBeGuessed:
                print("Success")
            else:
                guesses -= 1
                print(f"You have {guesses} left")
                numberByUser = int(input("Guess the number the cpu has decided: \n"))
    else:
        pass

    if guesses == 0:
        print(f"Number the cpu had chosen was {numberToBeGuessed}")
    else:
        return
    
guessNumber()
