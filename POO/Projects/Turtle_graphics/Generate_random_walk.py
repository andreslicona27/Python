import turtle
from turtle import Turtle
import random

t = Turtle()
turtle.colormode(255)

directions = [0, 90, 180, 270]
t.pensize(10)
t.speed("fastest")  # It can be managed as a string or as an integer


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for _ in range(200):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(directions))
