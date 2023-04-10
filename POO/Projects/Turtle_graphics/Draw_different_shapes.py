from turtle import Turtle
import random

t = Turtle()
t.shape("turtle")
t.goto(0, 80)
colors = ["blue", "red", "LightBlue", "green", "brown", "LightSeaGreen", "DarkOrchid", "CornflowerBlue", "yellow", "orange"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)


for shape_side_n in range(3, 11):
    t.color(random.choice(colors))
    draw_shape(shape_side_n)
