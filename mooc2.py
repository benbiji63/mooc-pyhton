# 2.1

# Fix the syntax

# number = int(input("Please type in a number: "))
# if number > 100:
#     print("The number was greater than one hundred")
#     number = number - 100
#     print("Now its value has decreased by one hundred")
#     print(f"Its value is now {number}")
# print(f"{number}  must be my lucky number!")
# print("Have a nice day!")

# Number of characters

# string = input("Please type in a word: ")
# lengthOfString = len(string)
# if lengthOfString > 1:
#     print(f"There are {lengthOfString} letters in the word hey")
# print("Thank you!")

# Typecasting

# import math

# num = float(input("Please type in a number: "))
# decimal_places = len(str(num).split(".")[1])

# parts = math.modf(num)

# integer_part = parts[1]
# decimal_part = round(parts[0],decimal_places)


# print(f"Integer part: {integer_part}")
# print(f"Decimal part: {decimal_part}")


# num = input("Please type in a number: ")
# parts = num.split(".")
# integer_part = parts[0]
# decimal_part = "0." + parts[1]

# print(f"Integer part: {integer_part}")
# print(f"Decimal part: {decimal_part}")


# 2.2

# Age of maturity

# age = int(input("How old are you?"))
# if age < 18:
#     print("You are not of age!")
# else:
#     print("You are of age!")


# Greater than or equal to

# num1 = int(input("Please type in the first number:"))
# num2 = int(input("Please type in another number:"))

# if num1 > num2:
#     print(f"The greater number was{num1}")
# elif num1 < num2:
#     print(f"The greater number was{num2}")
# else:
#     print("The numbers are equal!")


# The elder

# print("Person 1:")
# name1 = input("Name:")
# age1 = int(input("Age:"))
# print("Person 2:")
# name2 = input("Name:")
# age2 = int(input("Age:"))
# if age1 > age2:
#     print(f"The elder is{name1}")
# elif age1 < age2:
#     print(f"The elder is{name2}")
# else:
#     print(f'{name1} and {name2} are the same age')


# word1 = input("Please type in the 1st word:")
# word2 = input("Please type in the 2nd word:")

# if word1 == word2:
#     print("You gave the same word twice.")
# elif word1.lower() > word2.lower():
#     print(f"{word1} comes alphabetically last.")
# else:
#     print(f"{word1} comes alphabetically last.")


# 2.3

# Age check
# age = int(input("What is your age?"))

# if age >= 5:
#     print(f"Ok, you're {age} years old")
# elif age < 0:
#     print("That must be a mistake")
# else:
#     print("I suspect you can't write quite yet...")


# Nephews
# name = input("Please type in your name")
# if name == "Louie" or name == "Dewey" or name == "Huey":
#     print("I think you might be one of Donald Duck's nephews.")
# elif name == "Morty" or name == "Ferdie":
#     print("I think you might be one of the Mickey Mouse's nephew")
# else:
#     print("You're not a nephew of any character I know of.")

# Grade and Points

# points = int(input("How many points [0-100]:"))

# if points < 50 and points >= 0:
#     print("Grade: fail")
# elif points >= 50 and points < 60:
#     print("Grade: 1")
# elif points >= 60 and points < 70:
#     print("Grade: 2")
# elif points >= 70 and points < 80:
#     print("Grade: 3")
# elif points >= 80 and points < 90:
#     print("Grade: 4")
# elif points >= 90 and points <= 100:
#     print("Grade: 5")
# else:
#     print("Grade:impossible!")

# Leap Year

# year = int(input("Please type in a year:"))

# if year % 4 == 0 and year % 100 != 0:
#     print("That year is a leap year.")
# elif year % 400 == 0:
#     print("That year is a leap year.")
# else:
#     print("That year is not a leap year.")

# letter1 = input("1st letter:")
# letter2 = input("2nd letter:")
# letter3 = input("3rd letter:")
# middle = ""

# Alphabetically in the middle

# if letter1 < letter2 and letter3 < letter2:
#     if letter3 < letter1:
#         middle = letter1
#     else:
#         middle = letter3
# elif letter2 < letter3 and letter1 < letter3:
#     if letter2 < letter1:
#         middle = letter1
#     else:
#         middle = letter2
# elif letter3 < letter1 and letter2 < letter1:
#     if letter3 < letter2:
#         middle = letter2
#     else:
#         middle = letter3

# print(f"The letter in the middle is {middle}")

# Gift tax calculator


# def calcInterestAmount(giftValue, lowerLimit, baseValue, interestRate):
#     valueChange = giftValue - baseValue
#     rateChange = valueChange * interestRate
#     amountOfTax = lowerLimit + rateChange
#     print(f"Amount of tax: {amountOfTax} euros")


# valueOfGift = int(input("Value of gift: "))

# if valueOfGift < 5000:
#     print("No tax!")
# elif valueOfGift < 25000:
#     calcInterestAmount(valueOfGift, 100, 5000, 0.08)
# elif valueOfGift < 55000:
#     calcInterestAmount(valueOfGift, 1700, 25000, 0.1)
# elif valueOfGift < 200000:
#     calcInterestAmount(valueOfGift, 4700, 55000, 0.12)
# elif valueOfGift < 1000000:
#     calcInterestAmount(valueOfGift, 22100, 200000, 0.15)
# else:
#     calcInterestAmount(valueOfGift, 142100, 1000000, 0.17)


# 2.4

# Shall we continue?
# string = ""
# while string != "no":
#     print("hi")
#     string = input("Shall we continue")
# print("okay then")


# Input validation

# from math import sqrt

# num = 1
# while num!= 0 :
#     num = int(input("Please type in a number:"))
#     if num < 0:
#         print("Invalid number")
#     else:
#         break

# print("Exiting...")


# Fix the code: Countdown

# number = 5
# print("Countdown!")
# while True:
#   print(number)
#   number = number - 1
#   if number <= 0:
#     break

# print("Now!")


# Repeat password

# originalPassword = input("Password:")
# repeatedPassword = input("Repeat password:")

# while originalPassword != repeatedPassword:
#     print("They do not match!")
#     repeatedPassword = input("Repeat password:")

# print("User account created!")


# PIN and number of attempts

# attempts = 0
# while True:
#     attempts += 1
#     pin = input("PIN")
#     if pin == "4321":
#         break
#     print("Wrong")

# if attempts>1:
#     print(f"Correct! It took you {attempts} attempts")
# else:
#     print("Correct! It took you single attempts")


# The next leap year

# currrentYear = int(input("Year: "))
# nextLeapYear = currrentYear
# while True:
#     nextLeapYear += 1
#     if (nextLeapYear % 4 == 0 and nextLeapYear % 100 != 0) or nextLeapYear % 400 == 0:
#         break
# print(f"The next leap year after {currrentYear} is {nextLeapYear}")


# Story

# story = ""
# previousWord = ""
# while True:
#     word = input("Please type in a word: ")
#     if word == "end" or word == previousWord:
#         break
#     previousWord = word
#     story += word + " "

# print(story)


# Working with numbers

# print("Please type in integer numbers. Type in 0 to finish.")

# count = 0
# sum = 0
# positiveNumbers = 0
# negativeNumbers = 0


# while True:
#     number = int(input("Number: "))
#     if number == 0:
#         break
#     count += 1
#     sum += number
#     if number > 0:
#         positiveNumbers += 1
#     else:
#         negativeNumbers += 1

# mean = sum / count

# print("... the program asks for numbers")
# print(f"Numbers typed in {count}")
# print(f"The sum of the numbers is {sum}")
# print(f"The mean of the numbers is {mean}")
# print(f"Positive numbers {positiveNumbers}")
# print(f"Negative numbers {negativeNumbers}")

