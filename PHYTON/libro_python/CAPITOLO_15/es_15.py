"""
1. Above each line, write out in English what that line does.
2. If you are not sure, ask someone for help or search online. Many times searching for ”python3.6
THING” will find answers to what that THING does in Python. Try searching for ”python3.6 open.”
3. I used the word ”commands” here, but commands are also called ”functions” and ”methods.”
You will learn about functions and methods later in the book.
4. Get rid of the lines 10-15 where you use input and run the script again.
5. Use only input and try the script that way. Why is one way of getting the filename better than
another?

6. Start python3.6 to start the python3.6 shell, and use open from the prompt just like in this pro-
gram. Notice how you can open files and run read on them from within python3.6?

7. Have your script also call close() on the txt and txt_again variables. It’s important to close files
when you are done with them.
"""
#import a module
from sys import argv
#I assign to the variables the arguments passed at the time of the program execution
script, filename = argv
#open file
txt = open(filename)
#print use f.string
print(f"Here's your file {filename}:")
#print the contents of the file
print(txt.read())
txt.close()
"""
#name file in input
print("Type the filename again:")
file_again = input("> ")
#open the file
txt_again = open(file_again)
#print the contentsof the file
print(txt_again.read())
txt_again.close()
"""