'''
==============================
LICENSE AND COPYRIGHT NOTICE
==============================

snake-game-python
Copyright (C) 2024 vikalp-tyagi

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

For more information or to contact the author, please reach me at:
Email: vickyt.1309@gmail.com

See the GNU General Public License for more details:
Link: https://www.gnu.org/licenses/
'''

import turtle
import time
import random

# DELAY BETWEEN FRAMES
delay = 0.1

# SCREEN
screen_size = 650
screen = turtle.Screen()
screen.title("The Snake Game")
screen.bgcolor("orange")
screen.setup(width=screen_size, height=screen_size)
screen.tracer(0)

# GAME BOUNDARY
boundary_size = 250
turtle.speed(5)
turtle.pensize(5)
turtle.color('white')
turtle.penup()
turtle.goto(-boundary_size, boundary_size)
turtle.pendown()
for _ in range(4):
    turtle.forward(boundary_size * 2)
    turtle.right(90)
turtle.hideturtle()

# SNAKE
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

segments = []
segment_size = 20

# FOOD
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()

def place_food():
    """Randomly place the food."""
    x_cord = random.randint(-boundary_size + segment_size, boundary_size - segment_size)
    y_cord = random.randint(-boundary_size + segment_size, boundary_size - segment_size)
    food.goto(x_cord, y_cord)

place_food()

# SCOREBOARD
font = ("Courier", 25, "bold")
score, high_score = 0, 0

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white smoke")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, boundary_size + 10)

def update_score():
    scoreboard.clear()
    scoreboard.write(f"Score: {score}  High Score: {high_score}", align="center", font=font)

update_score()

# INSTRUCTIONS
instructions = turtle.Turtle()
instructions.speed(0)
instructions.color("white smoke")
instructions.penup()
instructions.hideturtle()
instructions.goto(0, - boundary_size - 50)
instructions.write("To Move: WASD/Arrow | To Quit: Q", align="center", font=font)

# MOVEMENT
def move():
    if head.direction == "up":
        head.sety(head.ycor() + segment_size)
    elif head.direction == "down":
        head.sety(head.ycor() - segment_size)
    elif head.direction == "left":
        head.setx(head.xcor() - segment_size)
    elif head.direction == "right":
        head.setx(head.xcor() + segment_size)

def set_direction(direction, opposite):
    if head.direction != opposite:
        head.direction = direction

# KEYBOARD BINDINGS
screen.listen()
keys = [
    ("up", "down", "Up"), ("down", "up", "Down"), ("left", "right", "Left"), ("right", "left", "Right"),
    ("up", "down", "w"), ("down", "up", "s"), ("left", "right", "a"), ("right", "left", "d")
]
for direction, opposite, key in keys:
    screen.onkeypress(lambda d=direction, o=opposite: set_direction(d, o), key)

quit_key = "q"
screen.onkeypress(lambda: screen.bye(), quit_key)

# RESET GAME
def reset_game():
    global score
    time.sleep(0.5)
    head.goto(0, 0)
    head.direction = "stop"
    [segment.goto(1000, 1000) for segment in segments]
    segments.clear()
    score = 0
    update_score()

# MAIN
while True:
    screen.update()

    # BORDER COLLISION
    if abs(head.xcor()) > boundary_size - segment_size or abs(head.ycor()) > boundary_size - segment_size:
        reset_game()

     # BODY COLLISION
    for segment in segments:
        if segment.distance(head) < segment_size:
            reset_game()

    # FOOD COLLISION
    if head.distance(food) < segment_size:
        score += 10
        if score > high_score:
            high_score = score
        update_score()
        place_food()
        
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("white smoke")
        new_segment.penup()
        segments.append(new_segment)

    # MOVE SEGMENTS
    for i in range(len(segments) - 1, 0, -1):
        x, y = segments[i - 1].pos()
        segments[i].goto(x, y)
    if segments:
        segments[0].goto(head.pos())

    move()
    time.sleep(delay)
