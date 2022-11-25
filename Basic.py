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

#__________________________________________________________________________________________________________________________________________________________________
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

#Multiplying a string by an integer, produces a repeated version of the original string. Like this:
print("spam" * 3) #spamspamspam
print(4 * '2') #2222

#Create a program to output "hi" 42 times, without any separators, on the same line.
print('hi'*42)

#You need to make a program for a leaderboard. The program needs to output the numbers 1 to 9, each on a separate line, followed by a dot:
print('''1.
2.
3.
4.
5.
6.
7.
8.
9.''')

print('1.\n2.\n3.\n4.\n5.\n6.\n7.\n8.\n9.')
#_______________________________________________________________________________________________________________________________________________

#Variables
#You can use letters, numbers, and underscores in variable names. But you can’t use special symbols, or start the name with a number.
#You can use the del statement to remove a variable. 
 #The provided code stores the value 7 in a variable, and outputs it. Change the code to output the value of the variable raised to the power of 3.
 # num = 7
 #print(num)
num = 7
print(num**3)

#!!!The input statement needs to be followed by parentheses!!! Even if the user enters a number as input, it's processed as a string:
x = input()
print("You entered: " + x)

#You can provide a string to input() between the parentheses, producing a prompt message.
name = input("Enter your name: ")
print("Hello, " + name) 

 #The following output needs to be produced: “name is age years old”, where name and age are variables.
name=input()
age=input() 
print(name + " is " + age + " years old")

#So we know that the input() function returns a string. To convert it to a number, we can use the int() function:
age = int(input())
print(age) 

#Similar to the int() function, the float() function converts a string to a float:
height = float(input())
print(height)

#str() function converts a number to a string.
age = 42
print("His age is " + str(age))

#you can use input() multiple times to take multiple user inputs.
name = input()
age = input()
print(name + " is " + age)

   #Write a program to take x and y as input and output the string x, repeated y times. Sample Input: hi, 3
x=input()
y=int(input())
print(x*y)

#In-place operators let you write code like 'x = x + 3' more concisely, as 'x += 3'.
x = "spam"
print(x)
x += "eggs"
print(x)  
#spam
#spameggs

#When you go out to eat, you always tip 20% of the bill amount. You’re making a program to calculate tips and save some time.
#Your program needs to take the bill amount as input and output the tip as a float.
bill = int(input())
print(bill*20/100)

#________________________________________________________________________

#Booleans 
#Booleans can have two values: True and False.
#We can create Booleans by comparing values, by using the equal operator ==
my_boolean = True
print(my_boolean)
#True

print(2 == 3)
#False

print("hello" == "hello")
#True

#Booleans are created when comparing values. Python has a number of comparison operators:
#equal to ==, not equal to !=, greater than >, smaller than <, greater or equal to >=, smaller or equal to <=.
x = 7
print(x != 8) #True
print(x > 5) #True
print(x < 2) #False
print(x >= 7) #True
print(x <= 7) #True

#Greater than and smaller than operators can also be used to compare strings lexicographically (the alphabetical order of words is based on the alphabetical order of their component letters). 
print(“hey” < “hay”) #False

#The True and False Boolean values can be represented as integers 1 and 0, respectively. 
#Note, that we used the int() function to convert the Boolean to an integer
x = (7 > 5)
print(int(x)) #1
#   _______________________________________

#if Statements

#One thing you can do with Booleans is use if statements to run code based on a certain condition, say, if the Boolean evaluates to True.
#An if statement looks like this:
#if condition:
    #statements
 
 #Python uses indentation (that empty space at the beginning of a line) to delimit blocks of code.
 #Depending on the program's logic, indentation can be mandatory.
 #The statements in the if should be indented.
 #The colon (:) at the end of the expression in the if statement is important, don’t leave it out.
x = 42
if x > 5:
   print("x is greater than 5")

spam = 7
if spam > 5:
   print("five")
if spam > 8:
   print("eight") #five
 
num = 12
if num > 5:
   print("Bigger than 5")
   if num <= 47:
      print("Between 5 and 47")
     

 #Write a program that checks if the water is boiling. Take the integer temperature in Celsius as input and output "Boiling" if the temperature is above or equal to 100.
temp = int(input())
if temp >= 100:
    print ('Boiling')
  






