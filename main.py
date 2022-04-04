import time
from player import Player
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, "Up")    

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()
