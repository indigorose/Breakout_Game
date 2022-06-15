from turtle import *
from paddle import Paddle
from ball import Ball
from bricks import Bricks
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=700, height=800)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)
"""X and Y border co-ordinates 
width = -300, 300
height = -350, 350
"""

# Draw bricks
bricks = Bricks()
bricks.create_brick()

# Draw Paddle
p_paddle = Paddle(0, -300)

# Move paddle
screen.listen()
screen.onkey(p_paddle.side_left, "Left")
screen.onkey(p_paddle.side_right, "Right")

# Draw Ball
ball = Ball()

# While loop for game play, move ball and detect ball contact, with bricks, paddles and wall.
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()
#   Brick detection - remove brick from game play and bounce
    for brick in bricks.all_bricks:
        if brick.distance(ball) < 20:
            brick.color("black")
            brick.goto(-400, -400)
            ball.bounce_y()
            scoreboard.update()
    # end game at no bricks left. if score is == 40
    if scoreboard.score == 40:
        scoreboard.reset()
        game_is_on = False
    # Detect collision with the wall
    if ball.xcor() < -300 or ball.xcor() > 300:
        ball.bounce_x()
    # Detection with top wall
    if ball.ycor() > 350:
        ball.bounce_y()
#   Detect collision with bottom paddle
    if ball.distance(p_paddle) < 50 and ball.ycor() > -350:
        ball.bounce_y()
#   Detect player paddle miss
    if ball.ycor() < -300:
        scoreboard.reset()
        game_is_on = False


screen.exitonclick()
