from turtle import Turtle

ALIGNMENT = "center"
FONT_SIZE = 24
FONT_TOP_BUFFER = 10
FONT = ("courier", FONT_SIZE, "normal")


class Scoreboard(Turtle):
    def __init__(self, game_screen_size):
        super().__init__()
        self.SCORE_TEXT_HEIGHT = int(game_screen_size / 2) - (FONT_SIZE + FONT_TOP_BUFFER)
        self.hideturtle()
        self.score = 0
        self.color('white')
        self.refresh()

    def increase_score(self):
        """adds one point to the score and refreshes the text"""
        self.score += 1
        self.refresh()

    def refresh(self):
        """clears the old score and writes the current one at the top of the screen"""
        self.clear()
        self.penup()
        self.setpos(x=0, y=self.SCORE_TEXT_HEIGHT)
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)
