from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import scoreb
import time

screen=Screen()
screen.setup(600,600)
screen.bgcolor("Black")
screen.title("My Snake game")
screen.tracer(0)

snake=Snake()
food=Food()
scor=scoreb()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.rigth,"Right")

ison=True
while ison:
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scor.increase()
    if snake.head.xcor() > 280 or snake.head.ycor() >280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        ison=False
        scor.gameover()
    for segments in snake.segments:
        if segments==snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            ison=False
            scor.gameover()
    snake.move()

screen.exitonclick()

