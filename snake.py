from turtle import Turtle

INITIAL_SIZE = 3
SEGMENT_SIZE = 20
STEP = SEGMENT_SIZE * 1
DIRECTION = {
    "UP": 90,
    "LEFT": 180,
    "DOWN": 270,
    "RIGHT": 0,
}


def initial_position(i):
    return -20.0 * i, 0.0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self, snake_size=INITIAL_SIZE):
        """creates snake. If no snake_size is given, it'll start at 3"""
        i = 0
        for _ in range(snake_size):
            self.add_segment(initial_position(i))
            i += 1

    def add_segment(self, seg_position):
        """creates a new snake segment and adds to the segments list"""
        snake_segment = Turtle(shape='square')
        snake_segment.penup()
        snake_segment.color('white')
        snake_segment.goto(seg_position)
        self.segments.append(snake_segment)

    def enlarge_snake(self):
        """increases the snake size"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """sets the snake in motion
        by moving it's head and repositioning every subsequent part
        to the position of the part immediately before it"""
        for n in range(len(self.segments) - 1, 0, -1):
            self.segments[n].goto(self.segments[n - 1].position())
        self.head.forward(STEP)

    def right(self):
        """redirects the snake's head to 0º"""
        if self.head.heading() != DIRECTION['LEFT']:
            self.head.seth(DIRECTION['RIGHT'])

    def up(self):
        """redirects the snake's head to 90º"""
        if self.head.heading() != DIRECTION['DOWN']:
            self.head.seth(DIRECTION['UP'])

    def left(self):
        """redirects the snake's head to 180º"""
        if self.head.heading() != DIRECTION['RIGHT']:
            self.head.seth(DIRECTION['LEFT'])

    def down(self):
        """redirects the snake's head to 270º"""
        if self.head.heading() != DIRECTION['UP']:
            self.head.seth(DIRECTION['DOWN'])
