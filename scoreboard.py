from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_alive = True
        self.score = 0
        with open('high_score.txt') as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("White")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=0, y=370)
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGN, font=FONT)

    def score_up(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGN, font=FONT)
        self.snake_alive = False
