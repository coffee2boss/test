import time
from car_manager import CarManager, COLORS
from player import STARTING_POSITION, Player
from turtle import Screen
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)


scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()


screen.listen()
screen.onkey(player.move, "Up")    

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()

    # create cars 2 MOVE by 5 paces
    car_manager.create_car()
    car_manager.move_cars()
    
    # goal on scoreboard
    if player.ycor() == 280:
        player.goto(STARTING_POSITION)
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

    # turtle gets run over
    for car in car_manager.all_cars:        # including all cars in the list with the turtle.
     if car.distance(player) < 20:
        game_is_on = False
        scoreboard.game_over()
    

screen.exitonclick()
