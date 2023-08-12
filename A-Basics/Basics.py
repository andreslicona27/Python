# ! DAY 1
# You have to use '' to print a message with quotation marks
print("hello" + " " + "'Andres'")
# It would ask the input before showing the complete message 
name = input("What is your name?")
length = len(name)  # To know the amount of characters of a string

print("Hello " + input("Write your name? ") + "!")
print(length)

# ! DAY 2
# ? PRIMITIVE DATA TYPES
print("hello"[0])  # Prints letter h
# 123_456_789 you can put "_" in numbers for it to be easier for you to read them

num = len(input("Whats your name?"))
print(type(num))  # Gives you the class of the variable
new_num = str(num)  # Converts the variable in a string
print(type(new_num))
print("your name has " + new_num + " characters")

a = float(100)

# Every time you divide you convert the type numbers to float 
# Use "**" to get the Exponential number 

print(round(10 / 3))  # for you to round numbers
print(round(10 / 3, 3))  # for you to round numbers with decimal places
print(round(10 // 3))  # gives you a integer

# f-String
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, and your are winning is {isWinning}")

# ! DAY 3
# ? Conditional statements help for coding not to overflow 
# ? if / elif / else and Multiple if
height = int(input(print("Give me your height in cm:")))
if height > 120:
    print("You can ride the roller coaster")
    age = int(input(print("Give me your age:")))
    if age < 12:
        bill = 5
        print("Child´s pay 5 ")
    elif age <= 18:
        bill = 7
        print("Young people pay 7")
    elif 35 <= age <= 45:
        bill = 7
        print("Ride without risk")
    else:
        bill = 12
        print("Adults pay 12")

    photo = input("Do you want a photo? Y / N")
    if photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("You have to be taller")

# ! DAY 4 
# ? Random & Lists
import random

random_integer = random.randint(100, 200)  # Returns a random number between the numbers you give him as parameters
# (including them both)
print(random_integer)

random_float = random.random() * 5
print(random_float)

# ? lists 
# fruits = [item1, item2]
# fruits.append()
# fruits.extend([item1, item2]) # allows to add multiple elements to a list
# fruits.insert(i,x)
# fruits.remove(x)

# ! DAY 5 
# ? For Loops
fruits = ["apple", "pears", "strawberries"]
for fruit in fruits:
    print(fruit)

# range function // does not include the second parameter 
total_sum = 0
for number in range(2, 101, 2):  # the last parameter is the steps que range made
    total_sum += number
print(total_sum)

# Gauss problem 
total = 0
for number in range(1, 101):
    total += number
print(total)


# ! DAY 6
# ? Functions
def my_function():
    print("Hello")
    print("Bye")


my_function()

# The block of code are creating with the indentation 
# ? While loop
print_message = 0
while print_message < 10:
    print("hello")

# ! DAY 7 Hangman project
# ! DAY 8  Function parameters  / Caesar Cipher
# ! DAY 9
# ? Dictionaries
# Define a dictionary of book information
book = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "published_year": 1960,
    "publisher": "J. B. Lippincott & Co.",
    "pages": 324
}
print(book["title"])  # show the value of a key
book["category"] = "fantasy"  # add new items to the dictionary
book["category"] = "science"  # this change the value, but if it does not exist it would create it

for key in book:
    print(key)
    print(book[key])

# ? Nesting
# is adding list or dictionaries inside dictionaries
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# ! DAY 10
# ? Functions with outputs
def format_name(fName, lName):
    if fName == "" or lName == "":
        return "Nothing to show"
    f_Name = fName.title()
    l_Name = lName.title()
    return f"{f_Name} {l_Name}"


# ! DAY 11 BlackJack
# ! DAY 12 Local and global scope (accessibility of variables)
# ? There is no block scope in python 
# ? the only way you cant access to a local variable it´s if it is inside a function

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1

# ? constants are always in capital letter

# ! DAY 13 Debugging
# ? Steps to identify bugs
# 1 Describe the problem 
# 2 Reproduce the bug 
# 3 Play computer (pretend to be one)
# 4 Fix the errors 
# 5 Print is you friend 
# 6 Use a Debugger
# EXTRA TIPS
# 7 take a break
# 8 Ask a friend
# 9 Run the code often
# 10 Ask Stack Overflow

# ! DAY 14 Higher lower game -project
# ! DAY 15 Install of Pycharm
