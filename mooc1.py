# 1.3

# Extra Spaces

# name = "Tim Tester"
# age = 20
# skill1 = "python"
# level1 = "beginner"
# skill2 = "java"
# level2 = "veteran"
# skill3 = "programming"
# level3 = "semiprofessional"
# lower = 2000
# upper = 3000

# print(f"my name is {name}, I am {age} years old \n")
# print("my skills are")
# print(f" - {skill1} ({level1})")
# print(f" - {skill2} ({level2})")
# print(f" - {skill3} ({level3}) \n")
# print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")

#  Arithmetics

# x = 15
# y = 27
# print(f"{x} + {y} = {x+y}")
# print(f"{x} - {y} = {x-y}")
# print(f"{x} * {y} = {x*y}")
# print(f"{x} / {y} = {x/y}")

# Fix the code: Print a single line

# print(5,end='')
# print(" + ",end='')
# print(8,end='')
# print(" - ",end='')
# print(4,end='')
# print(" = ",end='')
# print(5 + 8 - 4,end='')


# 1.4

# Times Five

# num = int(input("Please type in a number:"))
# print(f'{num} times 5 is {num*5}')

# Name and age

# name = input('What is your name?')
# year = int(input('Which year were you born?'))
# print(f'Hi {name}, you will be {2021-year} years old at the end of the year 2021')


# Seconds in a day

# noOfDays = int(input('How many days?'))
# print(f'Seconds in that many days: {noOfDays*60*60*24}')


# Fix the code: Product


# number1 = int(input("Please type in the first number: "))
# number2 = int(input("Please type in the second number: "))
# number3 = int(input("Please type in the third number: "))

# product = number1 * number2 * number3

# print("The product is", product)


# Sum and Product

# number1 = int(input("Number 1: "))
# number2 = int(input("Number 2: "))

# print(f"The sum of the numbers: {number1+ number2}")
# print(f"The product of the numbers: {number1 *number2}")

#  Students in Group

# import math

# noOfStudents = int(input("How many students on the course? "))
# groupSize = int(input("Desired group size? "))
# print(f"Number of groups formed: {math.ceil(noOfStudents/groupSize)} ")


# 1.5

# Orwell

# num = input('Enter a number')

# if num == '1984':
#   print('Orwell')

# Absolute value

# num = int(input("Enter a number"))

# if num >= 0:
#     print(f'The absolute value of this number is {num}')
# else:
#     print(f'The absolute value of this number is {num * -1}')

# Soup or no soup


# name = input("Please tell me your name:")

# if name != "Jerry":
#     portions = int(input("How many portions of soup?"))
#     price = 5.9 * portions
#     print(f"The total cost is {price}")

# print("Next please!")

# Calculator

# num1 = int(input("Number 1:"))
# num2 = int(input("Number 2:"))
# operation = input("Operation")
# if operation == "add":
#     print(f"{num1} + {num2} = {num1+num2}")

# elif operation == "subtract":
#     print(f"{num1} - {num2} = {num1-num2}")

# elif operation == "multiply":
#     print(f"{num1} * {num2} = {num1*num2}")


# Solving a quadratic equation

# from math import sqrt


# a=int(input('Value of a:'))
# b=int(input('Value of b:'))
# c=int(input('Value of c:'))

# root1 = (-b+sqrt((b**2)-(4*a*c)))/(2*a)
# root2 = (-b-sqrt((b**2)-(4*a*c)))/(2*a)

# print(f'The roots are {root1} and {root2}')
