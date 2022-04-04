from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12 , "normal")
FONT2 = ("Courier", 20 , "bold")

class Scoreboard(Turtle):

    def __init__(self):
    
            super().__init__()
            self.color("black")
            self.hideturtle()
            self.penup()
            self.score = 0
            self.update_scoreboard()
            

    def update_scoreboard(self):
        self.goto(0, 280)
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)
        

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT2)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


