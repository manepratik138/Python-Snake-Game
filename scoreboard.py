
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.game_is_over = False

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(
            f"Score: {self.score}",
            align="center",
            font=("Arial", 20, "normal")
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.game_is_over = True
        self.clear()

        self.goto(0, 30)
        self.write(
            "GAME OVER",
            align="center",
            font=("Arial", 30, "bold")
        )

        self.goto(0, -10)
        self.write(
            f"Final Score: {self.score}",
            align="center",
            font=("Arial", 18, "normal")
        )

        self.goto(0, -50)
        self.write(
            "Press R to Restart",
            align="center",
            font=("Arial", 15, "normal")
        )