from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Scoreboard

game_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_on:
    screen.update()
    time.sleep(0.1)

    snake.snake_move()

    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh_food()
        scoreboard.increase_score()
        snake.extend_snake()

    # DETECT COLLISION WITH WALL

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # DETECT COLLISION WITH TAIL
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
