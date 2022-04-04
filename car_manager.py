from turtle import Turtle
import random

Y_POSITIONS = [270, 260, 250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50 ,40, 30, 20, 10, 0, -250, -240, -230, -220, -210, -200, -190, -180, -170, -160, -150, -140, -130, -120, -110, -100, -90, -80, -70, -60, -50 ,-40, -30, -20, -10 ]
Y_POS = random.choice(Y_POSITIONS)
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DIST = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
         def __init__(self):
        
            super().__init__()
            self.color(random.choice(COLORS))
            self.shape("square")
            self.penup()
            self.speed("slowest")
            self.setheading(180)
            self.goto(300 ,Y_POS)
            self.move()
            
        

         def move(self):
            #for _ in range(MOVE_INCREMENT):                
            self.forward(STARTING_MOVE_DIST)
                #self.forward(MOVE_INCREMENT)
            