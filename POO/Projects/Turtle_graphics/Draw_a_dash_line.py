from turtle import Turtle

t = Turtle()
t.shape("turtle")
t.color("green")

# DRAW A DASH LINE
for _ in range(15):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
