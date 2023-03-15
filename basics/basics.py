#You have to use '' to print a message with quotation marks
print("hello" + " " + "'Andres'")
#It would ask the input before showing the complete message 
name = input("What is your name?")
length = len(name) #To know the amount of characters of a string 

print("Hello " + input("Write your name? ") + "!")

print(length)

#? PROJECT
print("Welcome to the Band Name Generator")
cityName = input("What's the name of the city you grew up in?\n")
petName = input("What's your pet's name?\n")
print("\nYour band name could be " + cityName + " " + petName)

#?PRIMITIVE DATA TYPES
print("hello"[0]) #Prints letter h 
#123_456_789 you can put "_" in numbers for it to be more easy for you to read them 

num = len(input("Whats your name?"))
print(type(num)) #Gives you the class of the variable 

new_num = str(num) #Converts the variable in a string
print(type(new_num))

print("your name has " + new_num + " characters")

a = float(100)

#Every time you divide you convert the type numbers to float 
#Use "**" to get the Exponential number 

print(round(10 / 3)) #for you to round numbers 
print(round(10 / 3, 3)) #for you to round numbers with decimal places 
print(round(10 // 3)) #gives you a integer 

#f-String
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, and your are winning is {isWinning}" )

