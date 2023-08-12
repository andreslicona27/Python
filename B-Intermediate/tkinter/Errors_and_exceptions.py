# try: something that might cause an exception
# except: do this if there was an exception
# else: do this if there were no exceptions
# finally: do this no matter what happens

try:
    file = open("a_file.txt")
    a_dictionary: dict[str, str] = {"key": "value"}
    print(a_dictionary["Hello"])

except FileNotFoundError:
    file = open("a_file.txt", "w")  # if its in writing mode it would create the dile in case it does not exist
    file.write("Something")

except KeyError as error_message:
    print(f"That key {error_message} does not exist")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("file was closed")
    raise TypeError("This is an error that i made up")  # i cant create my own exceptions


