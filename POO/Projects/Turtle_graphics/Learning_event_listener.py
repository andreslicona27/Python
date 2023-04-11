from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def turn_left():
    t.setheading(t.heading() + 10)


def turn_right():
    t.setheading(t.heading() - 10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
