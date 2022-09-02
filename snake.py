from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOV_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
WALL = [(-475, 375), (475, 375), (475, -395), (-475, -395), (-475, 375)]


class Snake:
    def __init__(self):
        self.wall = None
        self.make_wall()

        self.snake = []
        self.make_snake()
        self.head = self.snake[0]

    def make_wall(self):
        self.wall = Turtle()
        self.wall.hideturtle()
        self.wall.penup()
        self.wall.color("white")
        self.wall.width(5)
        for coordinates in WALL:
            self.wall.goto(coordinates)
            self.wall.pendown()

    def make_snake(self):
        for position in START_POS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.snake.append(new_segment)

    def increase_size(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            x_cor = self.snake[seg - 1].xcor()
            y_cor = self.snake[seg - 1].ycor()
            self.snake[seg].goto(x_cor, y_cor)
        self.head.fd(MOV_DIST)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.make_snake()
        self.head = self.snake[0]

    def mv_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def mv_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def mv_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def mv_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
