from turtle import Turtle


class scoreb(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("Red")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score : {self.score}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))
        self.goto(0,-24)
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))
    def increase(self):
        self.score+=1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))