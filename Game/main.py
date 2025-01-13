'''
snake-game-python
Copyright (C) 2024 vikalp-tyagi

For more information or to contact the author, please reach me at:
Email: vickyt.1309@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

See the GNU General Public License for more details.
<https://www.gnu.org/licenses/>
'''

import turtle
import random
import time

delay=0.1
score = 0
high_score = 0
    
#window
wn = turtle.Screen()
wn.title("The Snake Game")
wn.bgcolor("light green")
wn.setup(width=700, height=700)
wn.tracer(0)

#game_boundary
turtle.speed(5)
turtle.pensize(5)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('green')
turtle.forward(620)
turtle.right(90)
turtle.forward(520)
turtle.right(90)
turtle.forward(620)
turtle.right(90)
turtle.forward(520)
turtle.penup()
turtle.hideturtle()

#snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

#food
food = turtle.Turtle()
x_cord = random.randint(-290, 270)
y_cord = random.randint(-240, 240) 
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(x_cord, y_cord)

#scoreboard
scoreBoard = turtle.Turtle()
scoreBoard.speed(0)
scoreBoard.shape("square")
scoreBoard.color("white smoke")
scoreBoard.penup()
scoreBoard.hideturtle()
scoreBoard.goto(0, 260)
scoreBoard.write("Your Score: 0  Highest Score: 0", align="center",
        font=("Arial", 30, "bold"))

#movement
def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#keypress
wn.listen()
wn.onkeypress(move_up, "w")
wn.onkeypress(move_down, "s")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")

wn.onkeypress(move_up, "W")
wn.onkeypress(move_down, "S")
wn.onkeypress(move_left, "A")
wn.onkeypress(move_right, "D")

wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

#other
segments = []

while True:
    wn.update()

    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 230 or head.ycor() < -240:
        time.sleep(1)
        wn.clear()
        wn.bgcolor('light blue')
        scoreBoard.goto(0,0)
        scoreBoard.write("    GAME OVER\nYour Score is : {}".format(
            score), align="center", font=("Arial", 40, "bold"))

    if head.distance(food) < 20:
        score += 10
        if score > high_score:
            high_score = score
        scoreBoard.clear()
        scoreBoard.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("Arial", 25, "bold"))

        x_cord = random.randint(-270, 270)
        y_cord = random.randint(-230, 220) 
        food.speed(0)
        food.shape("circle")
        food.color("red")
        food.goto(x_cord, y_cord)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white smoke")
        new_segment.penup()
        segments.append(new_segment)

    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            wn.clear()
            wn.bgcolor('light blue')
            scoreBoard.goto(0,0)
            scoreBoard.write("    GAME OVER\nYour Score is : {}".format(
                score), align="center", font=("Arial", 40, "bold"))

    time.sleep(delay)

turtle.Terminator()
