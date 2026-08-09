import turtle as t
import random
t.penup()

colors = ["yellow","green","blue","red","orange","pink","purple"]

def hirst():
    def line():
        t.right(180)
        for i in range(10):
            randomcolor = random.choice(colors)
            t.dot(10,randomcolor)
            t.forward(20)
    for i in range(10):
        line()
        t.goto(0, t.ycor() + 20)
        t.right(180)
        
hirst()