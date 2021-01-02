from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self, game_barrier):
        super().__init__()
        self.GAME_BARRIER = game_barrier - 10
        self.penup()
        self.shape('circle')
        self.fillcolor('yellow')
        self.speed('fastest')  # effectively removes the repositioning animation
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.reposition()

    def reposition(self):
        """respawns the food somewhere else on screen"""
        self.goto(randint(-self.GAME_BARRIER, self.GAME_BARRIER), randint(-self.GAME_BARRIER, self.GAME_BARRIER))
