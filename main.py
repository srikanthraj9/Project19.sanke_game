from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("my snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # dectect collision with food
    if snake.head.distance(food) < 15:
       food.refresh()
       snake.extend()
       scoreboard.increase_score()

    #dectect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()
        # user_answer = screen.textinput(title="question", prompt="do want to play yes or no").lower()
        # if user_answer == "yes":
        #     is_game_on = True
        #     snake.head.goto(0, 0)

    for segment in snake.new_snake[1:]:
        if snake.head.distance(segment) < 5:
            is_game_on = False
            scoreboard.game_over()
            # user_answer = screen.textinput(title="question", prompt="do want to play yes or no").lower()
            # if user_answer == "yes":
            #     is_game_on = True
            #     snake.head.goto(0,0)

    print("Head position:", snake.head.position())
    for index, segment in enumerate(snake.new_snake):#The enumerate() function in Python is a handy tool for iterating through an iterable (like a list) while keeping track of both the index and the value of each element.
        print(f"Segment {index} position: {segment.position()}")
        print("Snake length:", len(snake.new_snake))



screen.exitonclick()