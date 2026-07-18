import random
from art import *

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices=[]
choices.extend([rock, paper, scissors])
myChoice = int(input("Enter your choice of turn: (0 for rock, 1 for paper, 2 for scissors) \n"))

while True:
    if myChoice > 2 or myChoice < 0:
        myChoice = int(input("Wrong command, try again. You can only choose 0 for rock, 1 for paper, 2 for scissors: \n"))
        break
    else:
        break

myChoiceVisual = choices[myChoice]
compChoiceVisual = random.choice(choices)
compChoice = choices.index(compChoiceVisual)

def game():
    if myChoice == 0:
        print(myChoiceVisual)
        if compChoice == 0:
            print(compChoiceVisual)
            print("Draw, both showed same figure. ")
        elif compChoice == 1:
            print(compChoiceVisual)
            print("Computer wins, paper covers rock. ")
        elif compChoice == 2:
            print(compChoiceVisual)
            print("You win, Rock smashes scissors. ")
        else:
            print("Error occured ")
    elif myChoice == 1:
        print(myChoiceVisual)
        if compChoice == 0:
            print(compChoiceVisual)
            print("You won. Paper covers rock. ")
        if compChoice == 1:
            print(compChoiceVisual)
            print("Draw, both showed same figure. ")
        if compChoice == 2:
            print(compChoiceVisual)
            print("You lost. Scissors cut paper")
        else:
            print("Error occured ")
    elif myChoice == 2:
        print(myChoiceVisual)
        if compChoice == 0:
            print(compChoiceVisual)
            print("You lost. Rock smashes scissors. ")
        elif compChoice == 1:
            print(compChoiceVisual)
            print("You won. Scissors cut paper. ")
        elif compChoice == 2:
            print(compChoiceVisual)
            print("Draw, both showed same figure. ")
    else:
        print("Error occured ")

game()