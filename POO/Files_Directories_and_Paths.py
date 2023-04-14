# ! DAY 24 Snake game has code example

# OPEN, CLOSE, READ, APPEND AND WRITE FILES
# The first method closes the file when you finish
# If you don't add the mode its in only reading
# 'w' stands for writing and 'a' stands for append in case you only want to add something
# If the file does not exist and is in write mode, one new file would be created
with open("my_file.txt", mode="w") as file:
    contents = file.read()
    file.write("")

file = open("my_file.txt")
file.close()

# SOME OTHER METHODS
variable = "Carlos"
PLACEHOLDER = "[name]"

variable.strip()  # removes all the spaces in the beginning and at the end
file.readlines()  # returns all the lines in the file by lines
file.replace(PLACEHOLDER, variable)

