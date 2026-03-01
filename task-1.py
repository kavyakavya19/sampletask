#Create three variables: one to store your name, one for your age, and one for your grade. Print them.
#Store True, 10, 3.14, and "Python" into four variables. Print their data types using type().
#Swap the values of two variables a = 5 and b = 10 without using a third variable.
#Declare a constant called PI with value 3.14159 and print it.
#Take a number input from the user and print whether the number is integer, float, or string type.

# a="kavya"
# b=20
# c="best"
# print(a,b,c)

# a="true"
# b=10
# c=3.14
# d="python"
# print(type(a),type(b),type(c),type(d))

# a=9
# b=19
# a,b=b,a
# print(a,b)

# PI=3.14159
# print(PI)

# a=int(input())
# print(type(a))

#Ask the user for two numbers and print their sum, difference, product, and average.
#Write an expression to check whether a number entered by the user is between 10 and 100 (inclusive).
#Check if a number entered by the user is even or odd using arithmetic operators.
#Write an expression to check if the sum of two numbers is greater than 50.
#Take two values from the user and print which one is greater or if they are equal.

# a=int(input("num 1:"))
# b=int(input("num 2:"))
# print("sum:",a+b)
# print("diff:",a-b)
# print("prod:",a*b)
# print("avg:",a/2)

# a=int(input("a:"))
# b=int(input("b:"))
# print(a+b>50)

# a=int(input("num 1:"))
# if a/2==0:
#     print("even")
# else:
#     print("odd")

# a=9
# b=19
# c=a+b
# if c>50:
#     print("greater thn 50")
# else:
#     print("less thn 50")

# a= int(input("Enter x: "))
# b= int(input("Enter y: "))
# if a>b:
#     print("a greater")
# elif a<b:
#     print("b greater")
# else:
#     print("Equal")

#expressions

# a=9
# b=19
# print((a*b)/b+a%b)
# print((a**b)%(a-b))
# print((a*b-a/b)+a)
# print((a and b))
# print(a or b)
# print(not a)


# Write a for loop to print all numbers from 1 to 10.
# Print all even numbers from 2 to 20 using a loop.
# Given the list fruits = ["apple", "banana", "cherry"], use a for loop to print each fruit.
# Use a for loop to print square of all numbers from 1 to n, where n is input by user.
# Write a loop that calculates the sum of all numbers from 1 to 100.


# for a in range(11):
#     print(a)

# for a in range(2,21,2):
#     print(a)

# a=["apple","banana","cherry"]
# for a in a:
#     print(a)

# a=int(input("Enter a:"))
# for i in range(1,a+1):
#     print(i*i)

# a=int(input("enter a:"))
# for i in range(1,101):
#     a+=i
# print(a)

# Write a while loop to print numbers from 10 down to 1.
# Using a while loop, keep asking the user to input a number until the user enters a number greater than 0.
# Write a while loop that prints all numbers between 1 and 30 that are divisible by 3.
# Ask the user how many times they want their name printed, then print the name that many times.
# Use a while loop to find the sum of digits of a number entered by the user.

# a=10
# while a>0:
#     print(a)
#     a-= 1

# while True:
#     num=int(input("Enter num>0: "))
#     if num > 0:
#         break

# a=1
# while a<=30:
#     if a%3==0:
#         print(a)
#     a+=1

# times=int(input("How many times? "))
# count=0
# while count<times:
#     print("kavya")
#     count += 1

# a=int(input("Enter num: "))
# b =0
# while a>0:
#     b +=a%10
#     a//=10
# print(b)

# Use nested loops to print a 3×3 grid of stars (*).
# Use nested loops to print this pattern:
# 1
# 22
# 333
# Print all pairs (i, j) where i goes from 1 to 3 and j goes from 1 to 4.
# Use nested loops to print the multiplication table from 1 to 5.
# Using nested loops, count how many times the digit 7 appears in the numbers from 1 to 100.

# for i in range(3):
#     for j in range(3):
#         print("*", end="")
#     print()

# for a in range(1,4):
#     print(str(a) * a)

# for a in range(1,4):
#     for b in range(1,5):
#         print(a, b)

# for a in range(1,6):
#     for b in range(1,6):
#         print(a*b, end=" ")
#     print()

# count7 = 0
# for a in range(1,101):
#     for b in str(a):
#         if b== "7":
#             count7 += 1
# print(count7)

# Write code that prints "Hello" at least once and then stops.
# Simulate a do-while to keep asking for a password until the user enters the correct one.
# Ask the user to enter numbers repeatedly until they enter 0, then print the sum of all entered numbers.
# Keep asking the user for a capital letter until they enter 'Q' or 'q'.
#  Simulate a loop that always runs at least once to ask a user to enter a positive number, and stops only when they give one


# while True:
#     print("Hello")
#     break

# while True:
#     pwd = input("Enter password: ")
#     if pwd == "secret":
#         break

# a= 0
# while True:
#     b= int(input("Enter number (0 to stop): "))
#     if b==0:
#         break
#     a+= b
# print(a)

# while True:
#     a= input("Enter letter: ")
#     if a.lower() == "q":
#         break

# while True:
#     a= int(input("Enter positive number: "))
#     if a>0:
#         break

#upper case,replace,count,find

# a="my name is kavya"
# print(a.upper())
# print(a.replace("a","k"))
# print("kavya"in a)
# print(a.count("k"))
# print(a.find("k"))

# a="kavya"
# print(len(a))

#slicing

# a=[1,2,3,4,5,6,7,8,9,10]
# print(a[:7])
# print(a[1:5])
# print(a[5:])
# print(a[::6])
# print(a[5::])
# print(a[:-5])

# Takes a sentence from the user.
# Converts the sentence into a list of words.
# Uses a loop to:
# Count how many words have more than 3 letters.
# Print:
# The list of words
# The number of words longer than 3 letters

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# count = 0
# for word in words:
#     if len(word) > 3:
#         count += 1
# print("List of words:", words)
# print("Number of words longer than 3 letters:", count)


# # 1.Create a tuple of 5 numbers.
# # Use a loop to print each number and find the sum of all numbers.
# #2. Create a tuple of 6 fruits.
# # Use a loop to count how many fruits have more than 5 letters.
# # 3.Take 4 numbers from the user and store them in a tuple.
# # Print the largest number using a loop.

# numbers = (2, 5, 8, 10, 3)
# total = 0
# for num in numbers:
#     print(num)
#     total += num
# print("Sum of numbers:", total)

# fruits = ("Apple", "Banana", "Cherry", "Mango", "Papaya", "Kiwi")
# count = 0
# for fruit in fruits:
#     if len(fruit) > 5:
#         count += 1
# print("Fruits with more than 5 letters:", count)

# numbers_input = input("Enter 4 numbers separated by spaces: ")
# numbers = tuple(int(x) for x in numbers_input.split())
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print("Largest number is:", largest)

# 1.Take a sentence from the user.
# Count how many vowels are in the sentence.
# 2.Take a word from the user.
# Reverse the string without using built-in reverse functions.
# 3.Take a sentence from the user.
# Count how many uppercase and lowercase letters are present.

# sentence = input("Enter a sentence: ")
# vowels = "aeiouAEIOU"
# count = 0
# for char in sentence:
#     if char in vowels:
#         count += 1
# print("Number of vowels:", count)

# word = input("Enter a word: ")
# reversed_word = ""
# for char in word:
#     reversed_word = char + reversed_word
# print("Reversed word:", reversed_word)

# sentence = input("Enter a sentence: ")
# upper_count = 0
# lower_count = 0
# for char in sentence:
#     if char.isupper():
#         upper_count += 1
#     elif char.islower():
#         lower_count += 1
# print("Uppercase letters:", upper_count)
# print("Lowercase letters:", lower_count)

# 1.Use a loop to print numbers from 1 to 20.
# 2.Use a loop to print the multiplication table of a given number.
# 3.Use a loop to find the factorial of a number.

# for i in range(1, 21):
#     print(i, end=" ")

# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print("Factorial of", num, "is", factorial)

# Takes a sentence from the user.
# Converts the sentence into a list of words.
# Converts that list into a tuple.
# Uses a loop to:
# Count how many words have more than 4 letters.
# Find the longest word.
# Create a new list of words that contain the letter 'a'.
# Print:
# The original list of words
# The tuple of words
# The count of words longer than 4 letters
# The longest word
# The list of words containing 'a'


# sentence = input("Enter a sentence: ")
# word_list = sentence.split()
# word_tuple = tuple(word_list) 
# count_long = 0
# longest_word = ""
# words_with_a = []
# for word in word_list:
#     if len(word) > 4:
#         count_long += 1
#     if len(word) > len(longest_word):
#         longest_word = word
#     if 'a' in word.lower():
#         words_with_a.append(word)
# print("List of words:", word_list)
# print("Tuple of words:", word_tuple)
# print("Number of words longer than 4 letters:", count_long)
# print("Longest word:", longest_word)
# print("Words containing 'a':", words_with_a)
