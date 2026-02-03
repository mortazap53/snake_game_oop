from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    snake.move()
    time.sleep(0.1)
    screen.update()






screen.exitonclick()