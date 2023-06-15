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


# This syntax's in know as syntactic sugar
@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


say_hello


# Advanced python decorator
class User:
    def __init__(self, name):
        self.name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}´s new blog post.")


new_user = User("Andres")
new_user.is_logged_in = True
create_blog_post(new_user)


# VARIABLES RULES
@app.route("username/<name>")
# @app.route("username/<path:name>")  # in this case in would return all the part that's after the name, including the name
def greet(name):
    return f"Hello {name}"  # You can add html code to create html elements


if __name__ == "__main__":
    app.run(debug=True)  # For you don't have to restart the file for every change
