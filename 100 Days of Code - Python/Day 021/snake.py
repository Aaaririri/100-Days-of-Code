from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
INITIAL_SIZE = 3
class Snake:
    """
    init the class with the size of the screen to make the borders of the screen invalid
    """
    def __init__(self, size_x = 600, size_y = 600):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head_x = self.head.xcor()
        self.head_y = self.head.ycor()
        self.screen_sizex = size_x/2
        self.screen_sizey = size_y/2

    def create_snake(self):
        pos = 0
        for i in range(INITIAL_SIZE):
            self.segments.append(Turtle("square"))
            self.segments[i].penup()
            self.segments[i].color("blue", "orange")
            self.segments[i].goto(pos, 0)
            pos = pos - 20

    def update_head(self):
        self.head_x = self.head.xcor()
        self.head_y = self.head.ycor()

    def snake_update(self):
        snake_x = self.segments[- 1].xcor()
        snake_y = self.segments[- 1].ycor()
        for i in range(len(self.segments) - 1, 0, -1):
            snake_x = self.segments[i - 1].xcor()
            snake_y = self.segments[i - 1].ycor()
            self.segments[i].goto(snake_x, snake_y)
        self.head.forward(MOVE_DISTANCE)
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("blue", "orange")
        new_segment.goto(snake_x, snake_y)
        self.segments.append(new_segment)
        self.update_head()

    def invalid_move(self):
        same_position = False
        if abs(self.head_x) >= self.screen_sizex:
            same_position = True
        elif abs(self.head_y) >= self.screen_sizey:
            same_position = True
        else:
            for i in range(1,len(self.segments)):
                if self.head.distance(self.segments[i]) <= 10:
                    same_position = True
        return same_position

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            snake_x = self.segments[i - 1].xcor()
            snake_y = self.segments[i - 1].ycor()
            self.segments[i].goto(snake_x, snake_y)
        self.head.forward(MOVE_DISTANCE)
        self.update_head()

    def arrow_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def arrow_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def arrow_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def arrow_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)