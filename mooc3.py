# 3.1


# Print numbers

# i = 2
# while i <= 30:
#     print(i)
#     i += 2

# Fix the code: Countdown

# print("Are you ready?")
# number = int(input("Please type in a number: "))
# while number != 0:
#     print(number)
#     number-=1
# print("Now!")

# Numbers

# i = 1
# number = int(input("Upper Limit: "))
# while i < number:
#     print(i)
#     i += 1


# Print numbers

# number = 2
# while number <= 30:
#     print(number)
#     number += 2

# Fix the code: Countdown

# print("Are you ready?")
# number = int(input("Please type in a number: "))
# while number > 0:
#     print(number)
#     number -= 1
# print("Now!")


# Numbers

# number = int(input("Upper Limit"))
# count = 1
# while count < number:
#     print(count)
#     count += 1


# Powers of base n

# upperLimit = int(input("Upper limit:"))
# base = 1
# power = base
# while power <= upperLimit:
#     print(power)
#     power *= base


# Powers of two

# upperLimit = int(input("Upper Limit: "))
# base = 1
# while base <= upperLimit:
#     print(base)
#     base*=2


# The sum of consecutive numbers, version 1

# limit = int(input("Upper Limit: "))
# base = 1
# increment = 2
# while base < limit:
#     base += increment
#     increment += 1
# print(base)


# The sum of consecutive numbers, version 2

# 'limit = int(input("Upper Limit: "))
# base = 1
# increment = 2
# str = "The consecutive sum: 1"
# while base < limit:
#     str += f" + {increment}"
#     base += increment
#     increment += 1

# print(str + f" = {base}")'


# 3.2

# String multiplied

# string= input('Please type in a string:')
# amount= int(input('Please type in an amount:'))
# print(string*amount)


# The longer string

# str1 = input("Please type in string 1: ")
# str2 = input("Please type in string 2: ")
# if len(str1) > len(str2):
#     print(f"{str1} is longer")
# elif len(str1) < len(str2):
#     print(f"{str2} is longer")
# else:
#     print("The strings are equally long")

# End to beginning

# string = input("Please type in a string:")
# index = -1
# while index >= -len(string):
#     print(string[index])
#     index -= 1


# Second and second to last characters

# string = input("Please type in a string:")
# if string[1] == string[-2]:
#     print(f"The second and the second to last characters are {string[1]}")
# else:
#     print("The second and the second to last characters are different")


# A line of hashes

# width = int(input("Width:"))
# print("#" * width)


# A rectangle of hashes

# width = int(input("Width:"))
# height = int(input("Height:"))

# for i in range(height):
#     print("#" * width)


# Underlining

# while True:
#     string = input("Please type in a string: ")
#     if string == "":
#         break
#     print(string)
#     print("-" * len(string))


# Right-aligned

# string = input("Please type in a string: ")
# stringLength = len(string)
# positionsToAlign = 20 - stringLength
# print("*" * positionsToAlign + string)


# A framed word

# content = input("Word: ")
# frame = "*" * 30
# spacesRequiredForLeftAlignment = int((28 - len(content)) / 2)
# spacesRequiredForRighftAlignment = spacesRequiredForLeftAlignment
# if len(content) % 2 != 0:
#     spacesRequiredForRighftAlignment += 1
# print(frame)
# print(
#     "*"
#     + " " * spacesRequiredForLeftAlignment
#     + content
#     + " " * spacesRequiredForRighftAlignment
#     + "*"
# )
# print(frame)


# Substrings, part 1

# string = input("Please type in a string:")
# i = 1
# limit = len(string)
# while i <= limit:
#     print(string[0:i])
#     i += 1


# Substrings, part 2

# string = input("Please type in a string: ")
# i = len(string) - 1
# while i >= 0:
#     print(string[i : len(string)])
#     i -= 1


# Does it contain vowels

# def findVowel(vowel, string):
#     if vowel in string:
#         print(f"{vowel} found")
#     else:
#         print(f"{vowel} not found")


# string = input("Please type in a string:")

# findVowel("a", string)
# findVowel("e", string)
# findVowel("o", string)

# Find the first substring

# word = input("Please type in a word: ")
# char = input("Please type in a character: ")

# indexOfChar = word.find(char)
# if len(word) - indexOfChar > 2:
#     print(word[indexOfChar : indexOfChar + 2])


# Find all the substrings

# word = input("Please type in a word: ")
# char = input("Please type in a character: ")

# while len(word) > 0:
#     indexOfChar = word.find(char)
#     if indexOfChar == -1:
#         break
#     if len(word) - indexOfChar > 2:
#         print(word[indexOfChar : indexOfChar + 3])
#     word = word[indexOfChar+1:]


# The second occurrence

# string = input("Please type in a string:")
# subString = input("Please type in a substring:")

# indexOfSubstring = string.find(subString)
# count = indexOfSubstring+len(subString)
# string = string[count :]
# indexOfSubstring = string.find(subString)

# if indexOfSubstring == -1:
#     print("The substring does not occur twice in the string.")
# else:
#   print(f'The second occurrence of the substring is at index {indexOfSubstring+count}.')


# 3.3

# Multiplication


# number = int(input("Please type in a number: "))

# for i in range(number):
#     for j in range(number):
#         print(f"{i+1} x {j+1} = {(i+1)*(j+1)}")


# First letters of words

# sentence = input("Please type in a sentence: ")
# while True:
#     print(sentence[0])
#     indexOfNextWord = sentence.find(" ")+1
#     sentence = sentence[indexOfNextWord:]
#     if indexOfNextWord < 1:
#         break


# factorial

# import math

# while True:
#     num = int(input("Please type in a number: "))
#     if num <= 0:
#         break
#     fact = math.factorial(num)
#     print(f"The factorial of the number 3 is {print}")

# print("Thanks and bye!")


# Flip the pairs

# number = int(input("Please type in a number: "))

# upper = 2
# lower = 1

# while True:
#     if upper > number:
#         break
#     print(upper)
#     print(lower)
#     upper += 2
#     lower += 2
# if number % 2 != 0:
#     print(lower)


# number = int(input("Please type in a number: "))

