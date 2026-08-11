from turtle import Turtle as t
START = [(0,0),(0,20),(0,40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class snake_game:
    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]

    def createsnake(self):
        for position in START:
            each_segment = t("square")
            each_segment.color("White")
            each_segment.penup()
            each_segment.goto(position)
            self.segments.append(each_segment)

    def movement(self):
        for segment_number in range(len(self.segments) -1, 0,-1):
            new_x = self.segments[segment_number-1].xcor()
            new_y = self.segments[segment_number -1].ycor()
            self.segments[segment_number].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def moveUp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def moveDown(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def moveLeft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def moveRight(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
