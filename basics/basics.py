
# ! DAY 1
# You have to use '' to print a message with quotation marks
print("hello" + " " + "'Andres'")
# It would ask the input before showing the complete message 
name = input("What is your name?")
length = len(name) #To know the amount of characters of a string 

print("Hello " + input("Write your name? ") + "!")

print(length)

# ! DAY 2
#?PRIMITIVE DATA TYPES
print("hello"[0]) #Prints letter h 
# 123_456_789 you can put "_" in numbers for it to be more easy for you to read them 

num = len(input("Whats your name?"))
print(type(num)) # Gives you the class of the variable 

new_num = str(num) # Converts the variable in a string
print(type(new_num))

print("your name has " + new_num + " characters")

a = float(100)

# Every time you divide you convert the type numbers to float 
# Use "**" to get the Exponential number 

print(round(10 / 3)) #for you to round numbers 
print(round(10 / 3, 3)) #for you to round numbers with decimal places 
print(round(10 // 3)) #gives you a integer 

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
    print("You can ride the rollercoaster")
    age = int(input(print("Give me your age:")))
    if age < 12:
        bill = 5
        print("Chields pay 5 ")
    elif age <= 18:
        bill = 7
        print("Young people pay 7")
    elif age >= 35 and age <= 45:
        bill= 7
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
 




