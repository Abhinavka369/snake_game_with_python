from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screener = Screen()
screener.setup(width=600, height=600)
screener.bgcolor("black")
screener.title("SNAKE GAME")
screener.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screener.listen()
screener.onkey(snake.up, "Up")
screener.onkey(snake.down, "Down")
screener.onkey(snake.left, "Left")
screener.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screener.update()
    time.sleep(.1)

    snake.move()
    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screener.exitonclick()
