import time

from flask import Flask

# FLASK
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# FIRST CLASS OBJECTS CAN BE PASSED AROUND AS ARGUMENTS
def add(n1, n2):
    return n1 + n2


def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


num_1 = 1
num_2 = 2
result = calculate(add, num_1, num_2)


# NESTED FUNCTIONS
def outer_function():
    print("outer")

    def nested_function():
        print("inner")

    nested_function()
    # Functions can be return from other functions
    # return nested_function()


outer_function()


# PYTHON DECORATOR
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before the function
        function()
        # Add functionality after doing the function
    return wrapper_function()


# this syntax's in know as syntactic sugar
@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


say_hello
