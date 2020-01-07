"""
1. If you do not understand this, go back through and use the comment trick to get it squared away
in your mind. One simple English comment above each line will help you understand or at least
let you know what you need to research more.
2. Write a script similar to the last exercise that uses read and argv to read the file you just created.
3. There’s too much repetition in this file. Use strings, formats, and escapes to print out line1, line2,
and line3 with just one target.write() command instead of six.
4. Find out why we had to pass a 'w' as an extra parameter to open. Hint: open tries to be safe by
making you explicitly say you want to write a file.
5. If you open the file with 'w' mode, then do you really need the target.truncate()? Read the
documentation for Python’s open function and see if that’s true.

4. w è passato come parametro all'apertura del file perchè serve per scrivere sul file
5. no perchè quando vado a scrivere su un file si cancella tutto ciò che conteneva
"""

#import a module
from sys import argv
#I assign to the variables the arguments passed at the time of the program execution
script, filename = argv
#print
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
#ask in input
input("?")
#open the file
print("Opening the file...")
target = open(filename, 'w')
# Empties the file
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
#ask in input
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
#write on the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#3.
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

#close the file
print("And finally, we close it.")
target.close()

#2.
from sys import argv
name=argv
content=open(name)
print("contenuto del file: " + content.read())