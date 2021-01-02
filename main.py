from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreborard import Scoreboard

# Game Setup
SPEED = 0.1
SCREEN_SIZE = 600
WALL_WIDTH = 10  # pixel width
game_on = True
GAME_BARRIER = int(SCREEN_SIZE / 2) - WALL_WIDTH
score = Scoreboard(SCREEN_SIZE)

# Screen Setup
screen = Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
screen.listen()

# Snake setup
snake = Snake()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Food setup
food = Food(GAME_BARRIER)


def move_snake():
    """while the game is on, updates the screen according to the game's set SPEED and moves the snake"""
    while game_on:
        screen.update()
        time.sleep(SPEED)
        detect_collision()
        snake.move()


def detect_collision():
    """triggers game_over when snake collides either with the game_barrier or it's own tail.
    Adds a score point in case of collision with food."""
    # with food
    if snake.head.distance(food) < 20:
        food.reposition()
        snake.enlarge_snake()
        score.increase_score()
    # with wall
    if snake.head.xcor() > GAME_BARRIER \
            or snake.head.xcor() < -GAME_BARRIER \
            or snake.head.ycor() > GAME_BARRIER \
            or snake.head.ycor() < -GAME_BARRIER:
        game_over()
    # with it's own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over()


def game_over():
    """triggers the 'GAME OVER' text and ends the game"""
    global game_on
    game_on = False
    score.game_over()
    # screen.onkey(replay, "space")


def replay():
    global game_on
    game_on = True


# Game initialization
move_snake()
# THE END
screen.exitonclick()
