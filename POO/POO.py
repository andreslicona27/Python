# ! DAY 16
# attribute is a variable inside a class
# method is a function inside a class

# import turtle
# timmy = turtle.Draw_a_spirograph.py() another form of doing it
from turtle import Turtle, Screen

# OBJECT
timmy = Turtle()
print(timmy)
timmy.shape("turtle")  # method
timmy.color("red")  # method
timmy.forward(100)  # method

# ATTRIBUTES
my_screen = Screen()
print(my_screen.canvheight)

# METHODS
my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)


# ! DAY 17
# PascalCase / camelCase / snake_case
class User:
    # pass # if you add a 'pass' declaration, it would let you create empty classes and functions
    def __init__(self, user_id, username):  # Constructor
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")
user_2 = User("002", "veronica")
user_1.follow(user_2)

# ! DAY 18 Turtle_graphics
# GUI graphical user interface
# ! DAY 19 Turtle_graphics continues
# ! DAY 20-21 Snake_Game
    #class Fish(Animal):
    #   def __init__(self):
    #      super().__init__()
    # this is how you inherits

# slicing tuples
piano_keys = ["a", "b", "c", "d", "e", "f"]
print(piano_keys[2:5:2])  # from 'c' to 'f' print every letter counting by two
print(piano_keys[::2])  # from beginning to end print every letter counting by two

# ! DAY 22 Pong Game
# ! DAY 23 Turtle Crossing Capstone



