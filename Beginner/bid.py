import os

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

names = []
bids = []

bidSet = {}

while True:
    bidName = input("Enter your name \n")
    bidValue = int(input("Enter the amount of bid you are willing to offer: \n"))
    bidContinue = input("Are there more people expected to involve in auction? (y/n) \n")
    if bidContinue == "y" or bidContinue == "yes":
        clearTerminal()
        names.append(bidName)
        bids.append(bidValue)
    elif bidContinue == "n" or bidContinue == "no":
        names.append(bidName)
        bids.append(bidValue)
        break
    else:
        print("Problem")
        break


highestBid = ""

highestBid = max(bids)
highestBidUser = bids.index(highestBid)
print(f"Highest bid was offered by: {names[highestBidUser]}")