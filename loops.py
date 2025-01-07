# <<<<<<<<<<<<<<<<<  loops  >>>>>>>>>>>>>>>.

# 1). contitional = if-else is not a loop. Instead, it is a conditional statement used to execute a block of Code 
#                   based on whether a condition is True or False. 
         
# 2). iterative = for = A for loop is used for iterating over a sequence (like a list, tuple, dictionary, set, or string
#                 while = A while loop executes as long as a specified condition is true

# 3). transfer = break: Exits the loop immediately.
#                continue: Skips the rest of the code for the current iteration and moves to the next one.
#                else: Executes when the loop finishes normally (without encountering break).




# <<<<<<<<<<<<<<<<<<<<<<<<<<<    if-else loop   >>>>>>>>>>>>>>>>>>>>>>>>>



# Write a program to check if a number entered by the user is positive, negative, or zero

# num = 5
# if num < 0:
#     print("num is positive and greater than or equals to six")
# else:
#     print("num is negative")      o/p = num is negative        


# Ask the user to enter their age and check if they are eligible to vote (18 or older)

# age = int(input("enter age: "))
# if age >= 18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible")


# Take a number as input and check if it is even or odd

# num = int(input("enter num: "))
# if num % 2 == 0:
#     print("num is even")
# else:
#     print("num is odd")



# Write a program that accepts three numbers and finds the largest among them

# a = int(input("enter a num: "))
# b = int(input("enter a num: "))
# c = int(input("enter a num: "))
# if a > b and a > c:
#     print("the largest num is: a")
# elif b > c:
#     print("the lagest num is: b")
# else:
    # print("largest num is: c")


# Ask the user to enter their exam score and display a grade:

# 90 and above: A
# 75 to 89: B
# 50 to 74: C
# Below 50: F

# marks = int(input("enter your marks: "))
# if marks >= 90:
#     print("grade a")
# elif marks >= 75 and marks <= 89:
#     print("grade b")
# elif marks >= 50 and marks <= 74:
#     print("grade c")
# else:
#     print("grade f")


# Take the temperature (in Celsius) as input and display:

# "Hot" if above 30
# "Pleasant" if between 20 and 30
# "Cold" if below 20

# temp = int(input("enter the temp in celsius: "))
# if temp > 30:
#     print("hot")
# elif 20 <= temp <= 30:
#     print("pleasent")
# else:
#     print("its cold")


# Check if a password entered by the user matches a pre-defined value.
#  Display a success message if it matches, otherwise display an error

# right_pass = "shreya123"
# password = (input("enter a password: "))
# if password == right_pass:
#     print("login")
# else:
#     print("error")



# Write a program to check if a specific substring (e.g., "Python") is present in a string
# str = "python is codding language"
# if "python" in str:
#     print("substring is python")
# else:
#     print("substring is not present")            substring is python



# Write a program to check if a number is:

# Less than 10
# Between 10 and 50
# Greater than 50
# num = 60
# if num < 10:
#     print("no is less than 10")
# elif 10 <= num <= 50:
#     print("no is between 10 and 50")
# else:
    # print("no is greater than 50")         no is greater than 50



# # Write a program to determine if a character is a vowel or a consonant
# char = 'e'
# if char in "aeiou":
#     print("vowel")
# else:
    # print("consonant")                          vowel



# # Write a program where the user guesses a number, and the program tells them if their guess is too high, too low, or correct
# guess_number = 50
# if guess_number < 50:
#     print("guess is too low")
# elif guess_number == 50:
#     print("corect")                            corect
# else:
#     print("too high")



# # Write a program to compare the lengths of two strings and print the longer one
# str1 = "hellow python"
# str2 = "python language"
# if len(str1) > len(str2):
#     print("the longer string is ",str1)
# elif len(str2) > len(str1):
#     print("the longer string is ",str2)                   the longer string is  python language
# else:
#     print("both are equal")                        


# str1 = "hellow python  "
# str2 = "python language"
# if len(str1) > len(str2):
#     print("the longer string is ",str1)
# elif len(str2) > len(str1):
#     print("the longer string is ",str2)
# else:
#     print("both are equal")                              both are equal



# Write a program to check if a number is prime.

# num = 13
# if num <= 1:
#     print("not prime no")
# elif num == 2:
#     print("not prime no")
# elif num % 2 == 0:
#     print("not prime no")
# else:
#     print("prime no")                                     prime no



# num = 13
# if num <= 1:
#     print("not prime no")
# elif num == 2:
#     print("not prime no")
# elif num % 2 == 1:
#     print("prime no")                                       prime no
# else:
    # print("not prime no") 



# Write a program to check if a number is zero or non-zero.
# num = 0
# if num == 0:
#     print("no is zero")
# else:
#     print("non zero")



# <<<<<<<<<<<<<<<<<<<<<<<<<<<    for loop   >>>>>>>>>>>>>>>>>>>>>>>>>



# word = "Python"

# for letter in word:
#     print(letter)
# o/p =
# P
# y
# t
# h
# o
# n



# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in numbers:
#     if num % 2 == 0:
#         print(num)

# output=
# 2
# 4
# 6
# 8
# 10

# for i in range(1, 11):
#     print(i)

# output=
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# # Write a program to print all numbers divisible by 3 between 1 and 50.
# for i in range(1,51):
#     if i % 3 == 0:
#         print(i)

# o/p = 
# 3
# 6
# 9
# 12
# 15
# 18
# 21
# 24
# 27
# 30
# 33
# 36
# 39
# 42
# 45
# 48


# Given a list of numbers, find the sum of all elements

# number = [10,20,10, 10 , 20, 20 ,40,50 , 30]
# total = 0
# for i in number:
#     total += i
# print("sum of number: ", total)


# Write a program to find the largest number in a list.

# numbers = [10,30, 70, 500, 75, 79, 6, 7777, 787]
# largest = numbers[0]

# for i in numbers:
#     if i > largest:
#         largest = i

# print("the largest number is: " , largest)


# #  Write a program to print each character of a string on a new line.

# name = "shreya"
# for char in name:
#     print(char)

# o/p =
# s
# h
# r
# e
# y
# a


# #  Print each fruit in the list fruits
# fruits = ["apple", "banana", "cherry", "kiwi"]
# for fruit in fruits:
#     print(fruit)    
# # output = apple
# # banana
# cherry
# kiwi


# # Print numbers from 1 to 5
# for i in range(1,6):
#     print(i)

# output = 1
# 2
# 3
# 4
# 5


# # Print each character in the string "hello"
# text = "hello"
# for char in text:
#     print(char, end =" ")                        h e l l o 

# text = "hello"
# for char in text:
#     print(char)   

# output  =   h
# e
# l
# l
# o              


# #  Print a 3x3 grid using nested loops.
# for i in range (3):
#     for j in range (3):
#         print((i, j),end = " ")
#     print()

# (0, 0) (0, 1) (0, 2) 
# (1, 0) (1, 1) (1, 2)
# (2, 0) (2, 1) (2, 2)



# Create a list of squares of numbers from 1 to 5
# squares = [x**2 for x in range(1, 6)]
# print(squares)                                     [1, 4, 9, 16, 25]


# Print even numbers from 1 to 10
# for i in range (1,11):
#     if i % 2 == 0:
#         print(i)                                   
# 2
# 4
# 6
# 8
# 10


# stop the loop when a number equals 5
# for i in range(1,10):
#     if i == 5:
#         break
#     print(i, end = " ")                           1 2 3 4 


# Skip the number 5 in a loop
# for i in range(1,10):
#     if i == 5:
#         continue
#     print(i, end = " ")                             1 2 3 4 6 7 8 9 



# Print elements with their indices from a list
# names = ["shreya", "shruti", "swaraj", "anshu", "shivraj"]
# for index, name in enumerate(names):
#     print("Index", index, ":", name)

# Index 0 : shreya
# Index 1 : shruti
# Index 2 : swaraj
# Index 3 : anshu
# Index 4 : shivraj


# Print numbers from 10 to 1 in reverse.
# for i in range(10,0,-1):
#     print(i, end = " ")                              10 9 8 7 6 5 4 3 2 1


# Print numbers from 0 to 20 with a step of 5.
# for i in range(0,21,5):
#     print(i)

# 0
# 5
# 10
# 15
# 20


# for i in range(1,10):
#      if i == 5:
#         pass
#      print(i, end = " ")                1 2 3 4 5 6 7 8 9 




# <<<<<<<<<<<<<<<<<<<<<<<< while loop >>>>>>>>>>>>>>>>>>>>>>>>>>>

# while is reserve keyword
# while loop used for repetition
# while loop depends on condition

# syntax------
# #start
# #condition (with while)
# #increment/decrement



# i = 1
# while i <= 10:
#     print(i,"hello")
#     i = i + 1

# print(i)

# 1 hello
# 2 hello
# 3 hello
# 4 hello
# 5 hello
# 6 hello
# 7 hello
# 8 hello
# 9 hello
# 10 hello
# 11

# i = 10
# while i >= 1:
#     print(i,"hello")
#     i = i - 1

# print(i)

# output=
# 10 hello
# 9 hello
# 8 hello
# 7 hello
# 6 hello
# 5 hello
# 4 hello
# 3 hello
# 2 hello
# 1 hello
# 0



# Write a while loop that prints numbers from 0 to 4.

# count = 0
# while count < 5:
#     print("Count:", count)
#     count += 1

# Count: 0
# Count: 1
# Count: 2
# Count: 3
# Count: 4


# i = 0
# while i <= 10:
#     print(i, "shreya")
#     i = i + 1

# print(i)

# 0 shreya
# 1 shreya
# 2 shreya
# 3 shreya
# 4 shreya
# 5 shreya
# 6 shreya
# 7 shreya
# 8 shreya
# 9 shreya
# 10 shreya
# 11


# Write a while loop to print the first 5 even numbers starting from 0.

# num = 0
# count = 0
# while count < 5:
#     print(num, end = " ")
#     num += 2
#     count += 1                                0 2 4 6 8 


# Write a while loop to calculate the sum of the first 10 natural numbers.

# num = 0
# sum = 0
# while num <= 10:
#     sum += num
#     num += 1
# print("Sum:", sum)                           Sum: 55



