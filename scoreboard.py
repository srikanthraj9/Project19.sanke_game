from turtle import Turtle
alignment = "center"
front = ("Arial", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
      self.write(f"score:{self.score}", align=alignment, font=front)

    def game_over(self):
        self.goto(0,0)
        self.write("game over", align=alignment,font=front)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
