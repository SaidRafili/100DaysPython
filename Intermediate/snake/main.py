from turtle import Turtle as t
from turtle import Screen
from snake import snake_game
import time

screen = Screen()
screen.bgcolor("Black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

Snake = snake_game()

screen.listen()
screen.onkey(Snake.moveUp, "Up")
screen.onkey(Snake.moveDown, "Down")
screen.onkey(Snake.moveLeft, "Left")
screen.onkey(Snake.moveRight, "Right")

while True:
    screen.update()
    time.sleep(1 / 15)
    Snake.movement()

screen.exitonclick()