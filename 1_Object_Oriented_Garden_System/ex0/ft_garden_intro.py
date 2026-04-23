#    Main script
#        - Sets the plant information in variables
#        - Print welcoming message
#        - Print plant informations
#        - Signalize the end of the function

def main():
    name = "Rose"
    height = 25
    age = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}\nHeight: {height}cm\nAge: {age} days\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    main()

# When a file is run as a script, it sets the __name__ as "__main__",
# otherwise it will be set as the filename and considered an import.
# The if __name__ == "__main__" is used to allow the creation of a file that
# can be both imported as a module or executed as a standalone script.
#   This is good when being able to execute the script is necessary/useful,
#   but you don't want that being executed when the file is imported, for
#   example when creating Unit tests

# A 'shebang' is something used to tell the operating system which interpreter
# should be used to execute the code, which can be helpful when intended to
# execute the script accross different operating systems.
# Allowing to run it without needing to specify it, just as the example bellow:
#   python ex0/ft_garden_intro.py (without the #!/usr/bin/python3)
#   ex0/ft_garden_intro.py
