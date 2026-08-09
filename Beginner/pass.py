import random

letters = ["a","b","c",'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ["1","2","3","4","5","6","7","8","9","0"]
chars = ["!",",",".","*","-","?","&","+","(",")"]

def generate():
    amountOfLetters =  int(input("How many letters would you like to use? \n"))
    amountOfNumbers = int(input("How many numbers do you want to include? \n"))
    amountOfChars = int(input("Number of characters you would like to use: \n"))
    lettersIncluded = []
    numbersIncluded = []
    charsIncluded = []
    for _ in range(amountOfLetters):
        lettersIncluded.append(random.choice(letters))
    for _ in range(amountOfNumbers):
        numbersIncluded.append(random.choice(numbers))
    for _ in range(amountOfChars):
        charsIncluded.append(random.choice(chars))
    mergedPassword = lettersIncluded + numbersIncluded + charsIncluded
    random.shuffle(mergedPassword)
    print(''.join(mergedPassword))

generate()