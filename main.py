import time
from turtle import Screen

from apple import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.title('Snake')
screen.bgcolor('black')
screen.tracer(0)

my_snake = Snake()
apple = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key='Left', fun=my_snake.mv_left)
screen.onkey(key='Right', fun=my_snake.mv_right)
screen.onkey(key='Up', fun=my_snake.mv_up)
screen.onkey(key='Down', fun=my_snake.mv_down)
screen.onkey(key='s', fun=scoreboard.game_over)

while scoreboard.snake_alive:
    # Keep Moving
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    # Eat Apple
    if apple.distance(my_snake.head) < 15:
        apple.refresh()
        scoreboard.score_up()
        my_snake.increase_size()
        my_snake.move()

    # Detect Wall collision
    if my_snake.head.xcor() > 475 or my_snake.head.xcor() < -475 or \
            my_snake.head.ycor() > 375 or my_snake.head.ycor() < -395:
        scoreboard.reset()
        my_snake.reset()

    # Detect snake self body collision
    for segment in my_snake.snake[1:]:
        if my_snake.head.distance(segment) < 10:
            scoreboard.reset()
            my_snake.reset()

screen.exitonclick()
