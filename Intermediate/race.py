import turtle as t
import random
from tkinter import messagebox

screen = t.Screen()
colors = ["yellow","green","blue","red","orange","pink","purple"]
racers = []
for i in range(7):
    racer = t.Turtle()
    racers.append(racer)
    racer.penup()
    racer.speed("fastest")
    racer.color(colors[i])
    racer.shape("turtle")
    racer.setx(-200)
    racer.sety(i * 40)

def startRace():
    while True:
        randomracer = racers[random.randint(0,6)]
        newposition = randomracer.xcor()
        randomracer.goto(randomracer.pos() + (random.randint(1,10),0))
        if newposition == 0:
            break
            
    def get_turtles_at_x():
        import turtle as t
        screen = t.Screen()
        
        for t in screen.turtles():
            if t.xcor() >= 0:
                winning_color = t.pencolor()
                print(winning_color)

    
        
    get_turtles_at_x()



startPermission = screen.textinput("Greetings" , "Would you like to start the race")
if startPermission == "yes" or "y":
    bet = screen.textinput("Bet on turtles", "Which turtle do you think will win?")
    startRace()
else:
    pass
