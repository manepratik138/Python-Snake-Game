
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = None
food = None
scoreboard = None
game_is_on = False


def start_game():
    global snake, food, scoreboard, game_is_on

    # Remove the previous game objects
    if snake is not None:
        for segment in snake.segments:
            segment.hideturtle()

    if food is not None:
        food.hideturtle()

    if scoreboard is not None:
        scoreboard.hideturtle()
        scoreboard.clear()

    snake = Snake()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    food = Food()
    scoreboard = Scoreboard()

    game_is_on = True
    game_loop()


def game_loop():
    global game_is_on

    if not game_is_on:
        return

    screen.update()
    snake.move()

    # Food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Wall collision
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()
        screen.update()
        return

    # Self collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            screen.update()
            return

    screen.ontimer(game_loop, 100)


def restart_game():
    if not game_is_on:
        start_game()


screen.listen()
screen.onkey(snake.up if snake else lambda: None, "Up")
screen.onkey(snake.down if snake else lambda: None, "Down")
screen.onkey(snake.left if snake else lambda: None, "Left")
screen.onkey(snake.right if snake else lambda: None, "Right")
screen.onkey(restart_game, "r")
screen.onkey(restart_game, "R")

start_game()

screen.mainloop()