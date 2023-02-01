from turtle import Turtle

class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 15
        self.y_move = 15
        self.move_speed = 0.1

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def ybounce(self):
        self.y_move *= -1

    def xbounce(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.xbounce()
        self.move_speed = 0.1
