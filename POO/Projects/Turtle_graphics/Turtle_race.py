from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter the color: ")
colors = ["red", "blue", "green", "orange", "yellow", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
is_race_on = False
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You´ve won! The {winning_color} turtle is the winner!")
            else:
                print(f"You´ve lost! The {winning_color} turtle is the winner!")

        turtle.forward(random.randint(0, 10))



screen.exitonclick()
