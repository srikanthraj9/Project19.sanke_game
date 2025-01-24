from turtle import Turtle

# new_snake = []
# def snake():
#     snake_position = [(0, 0), (-20, 0), (-40, 0)]
#     global new_snake
#     for position in snake_position:
#         snake = Turtle("square")
#         snake.color("white")
#         snake.penup()
#         snake.goto(position)
#         new_snake.append(snake)
#
# def move():
#     global new_snake
#     for snake_num in range(len(new_snake)-1,0,-1 ):
#         new_x = new_snake[snake_num - 1].xcor()
#         new_y = new_snake[snake_num - 1].ycor()
#         new_snake[snake_num].goto(new_x,new_y)
#     new_snake[0].forward(20)
#     new_snake[0].left(90)


snake_position = [(0, 0), (-20, 0), (-40, 0)]
moving_speed = 10
left = 180
right = 0
up = 90
down = 270
class Snake:
    def __init__(self):
        self.new_snake = []
        self.create_snake()
        self.head = self.new_snake[0]


    def create_snake(self):
        for position in snake_position:
            self.add_snake(position)

    def add_snake(self,position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.new_snake.append(snake)

    def extend(self):
        self.add_snake(self.new_snake[-1].position())  # position() method from turtle model



    def move(self):
        for snake_num in range(len(self.new_snake) - 1, 0, -1):
            new_x = self.new_snake[snake_num - 1].xcor()
            new_y = self.new_snake[snake_num - 1].ycor()
            self.new_snake[snake_num].goto(new_x, new_y)
        self.head.forward(moving_speed)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)





