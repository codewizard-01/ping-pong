from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        y_position = self.ycor() + 20
        self.goto(self.xcor(), y_position)

    def go_down(self):
        y_position = self.ycor() - 20
        self.goto(self.xcor(), y_position)

