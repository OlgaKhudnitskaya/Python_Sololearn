# Doing a calculation in Python is simple, just enter it into the print statement:
print(2 + 2)
print(5 + 4 - 3)
print(12 * 64)
print(100 / 2) # when dividing two integers produces a decimal, which is called a float 50.0
print(2 * (3 + 4))
print(-8 * 6)
print((-5 - 1) * 3)
print(2**5) # Two asterisks ** are used to raise a number to the power of another, which is called exponentiation
print(9 ** (1 / 2)) #The result will be a float. 3.0
print(20 // 6) # In case we want to find the quantity produced by the division of two numbers as an integer (also called the quotient), we can use the floor division operator //: The code above will output 3, because 6 goes into 20 three times.
print(20 % 6) #If we want to find only the remainder in a division, we use the modulo operator % output - 2

#The team won 18 games and ended 7 games as a draw.
#A win brings 3 points, while a draw brings 1.
#Create a program to calculate and output the total points earned by the team.
print((18 * 3) + (7 * 1))


# There are situations where you might want to print multiple messages in your code.
# Each print statement outputs text in a new line.
print("Shopping List:")
print('Bread')
print("Eggs")

print("42") #In the code, 42 is a string, not an integer.

#In Python, the backslash \ is a special character, called the escape character.It is used to represent certain things in a string, such as new lines, tabs, and other useful things.
print('Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!')
print("\t hey \t there") #Similar to a new line, we can create a tab using \t
print("Hi \r there") #\r is used to shift the cursor to the beginning of the line, however it might not work as expected in all Python environments.
print("Newline is \\n") #What if we need to include the special character in our output? For example, what if we want to have \n in the output
#\n is the newline character, while \r is the carriage return. They differ in what uses them. 
#Windows uses \r\n to signify the enter key was pressed, while Linux and Unix use \n.

print("""this
is a
multiline
text""")
#Newlines are automatically added for strings created using three quotes.
print('''
I'm learning.
Python's syntax is easy.
''')

#Write a program to output the letters A B C D, each on a separate line.
#You can use 3 quotes to add the new lines.
print('''A
B
C
D''')

