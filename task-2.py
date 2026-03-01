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


# TYPE CASTING & CONVERSION PROBLEMS
# 🟢 Basic
# Convert a string "123" into an integer and add 10.
# Convert a float 12.56 into an integer.
# Convert an integer to a string and concatenate it with another string.
# Convert a list into a tuple.
# Convert a tuple into a list.

# a="123" 
# a=int(a)
# print(a+10)

# a=12.56
# a=int(a)
# print(a)

# a=919
# b="27"
# a=str(a)
# c=(a+""+b)
# print(c)

# a=[1,2,3,4,5]
# a=tuple(a)
# print(a)

# a=(1,2,3,4,5)
# a=list(a)
# print(a)

# 🟡 Intermediate
# Take user input (string) and convert it to an integer. Check if it's even or odd
# Convert a list of string numbers ["1", "2", "3"] into integers.
# Convert a dictionary keys view into a list.
# Convert a string "True" into a boolean.
# Convert a set into a list and sort it.

# a="9"
# a=int(a)
# if a%2==0:
#     print("even")
# else:
#     print("odd")

# a=["1","2","3"]
# a=list(map(int,a))
# print(a)

# a={"name":"kavya","age":21,"gender":"female"}
# b=a.keys()
# a=list(a)
# print(a)

# a="true"
# b=a=="true"
# print(b)

# a={1,7,9,4,5}
# b=list(a)
# b.sort()
# print(b)

# 🔴 Advanced
# Convert a sentence into a list of words, then into a tuple.
# Convert two lists into a dictionary using type conversion.
# Convert a binary string (e.g., "1010") into a decimal number.
# Convert a decimal number into binary (without using bin())
# Convert a list of tuples into a dictionary.

# a="my name is kavya"
# b=a.split()
# c=tuple(b)
# print(c)

# a=["name","age","grade"]
# b=["kavya",21,"female"]
# c=dict(zip(a,b))
# print(c)

# a="1010"
# b=int(a,2)
# print(b)

# a= 10
# b= ""
# while a>0:
#     remainder = a%2       
#     b= str(remainder)+b
#     a=a//2        
# print("b:",b)

# a=[("name","kavya"),("age",21),("gender","female")]
# b=dict(a)
# print(a)

# Problem 1 – Employee Salary Lookup
# Create a dictionary that stores employee names as keys and their salaries as values.
# Ask the user to input an employee name and print their salary.
# If the employee doesn’t exist, print "Employee not found"


# emp = {"a": 5, "b": 6, "c": 7, "d": 8, "e": 9}
# name = input("Enter employee name: ")
# if name in emp:
#     print(f"{name}'s salary is: {emp[name]}")
# else:
#     print("Employee not found")

# Problem 2 – Count Word Frequency
# Write a program that takes a sentence and counts the frequency of each word using a dictionary.
# Example input: "apple banana apple orange banana apple"
# Expected output: {'apple': 3, 'banana': 2, 'orange': 1}

# sentence = "apple banana apple orange banana apple"
# words = sentence.split()
# freq = {}
# for word in words:
#     freq[word] = freq.get(word, 0) + 1
# print(freq)

# Problem 3 – Merge Two Dictionaries
# You have two dictionaries with product prices:
# dict1 = {"apple": 50, "banana": 20}
# dict2 = {"banana": 30, "orange": 40}
# Merge the dictionaries.
# If a product exists in both, sum their prices.

# dict1 = {"apple": 50, "banana": 20}
# dict2 = {"banana": 30, "orange": 40}
# merged_dict = dict1.copy()
# for key, value in dict2.items():
#     if key in merged_dict:
#         merged_dict[key] += value
#     else:
#         merged_dict[key] = value
# print(merged_dict)

# Problem 4 – Students Above Average
# Given a dictionary of students and their marks, print the names of students whose marks are above the average.
# Example: {"Alice": 85, "Bob": 90, "Charlie": 78, "David": 92}

# students = {"Alice": 85, "Bob": 90, "Charlie": 78, "David": 92}
# average = sum(students.values()) / len(students)
# for name, marks in students.items():
#     if marks > average:
#         print(name)

# Problem 5 – Group Items by Category
# You have a list of tuples representing items and their categories:
# items = [("apple", "fruit"), ("carrot", "vegetable"), ("banana", "fruit")]
# Create a dictionary that groups items by category.
# Expected output: {"fruit": ["apple", "banana"], "vegetable": ["carrot"]}

# items = [("apple", "fruit"), ("carrot", "vegetable"), ("banana", "fruit")]
# grouped = {}
# for item, category in items:
#     if category not in grouped:
#         grouped[category] = []
#     grouped[category].append(item)
# print(grouped)

# 1. Unique Elements
# Given a list of numbers, remove duplicates using a set.
# Example: [1, 2, 2, 3, 4, 4] → {1, 2, 3, 4}
# 2. Common Elements
# Given two lists, find the common elements using sets.
# Example: [1,2,3,4] and [3,4,5,6]
# 3. Set Length
# Create a set from a list and print the number of unique elements.
# 4. Add & Remove
# Create a set of fruits. Add a new fruit and remove one existing fruit.

# numbers = [1, 2, 2, 3, 4, 4]
# unique_numbers = set(numbers)
# print(unique_numbers)

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# common = set(list1) & set(list2)
# print(common)

# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique_numbers = set(numbers)
# print(len(unique_numbers))

# fruits = {"apple", "banana", "orange"}
# fruits.add("grape")
# fruits.remove("banana")
# print(fruits)

# 5. Union of Sets
# Given two sets, find their union.
# 6. Intersection of Sets
# Find the intersection of two sets.
# 7. Difference Between Sets
# Find elements that are present in set A but not in set B.
# 8. Symmetric Difference
# Find elements that are in either set A or set B but not in both.

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set1 | set2
# print(union_set)

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# intersection_set = set1 & set2
# print(intersection_set)

# setA = {1, 2, 3, 4}
# setB = {3, 4, 5}
# difference = setA - setB
# print(difference)

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# sym_diff = set1 ^ set2
# print(sym_diff)


# 9. Subset Check
# Check whether one set is a subset of another.
# 10. Remove Duplicates from Sentence
# Given a sentence, print all unique words using sets.
# 11. Count Vowels
# Given a string, use a set to count unique vowels present.
# 12. Students in Both Courses
# Given two sets representing students in two courses, find:
# Students enrolled in both
# Students enrolled in only one course
# All students enrolled

# setA = {1, 2}
# setB = {1, 2, 3, 4}
# print(setA.issubset(setB))

# sentence = "apple banana apple orange banana"
# words = sentence.split()
# unique_words = set(words)
# print(unique_words)

# text = "programming"
# vowels = set("aeiou")
# found_vowels = set()
# for char in text:
#     if char in vowels:
#         found_vowels.add(char)
# print("Unique vowels:", found_vowels)
# print("Count:", len(found_vowels))

# course1 = {"Alice", "Bob", "Charlie"}
# course2 = {"Bob", "David", "Charlie"}
# both_courses = course1 & course2
# only_one = course1 ^ course2
# all_students = course1 | course2
# print("Both courses:", both_courses)
# print("Only one course:", only_one)
# print("All students:", all_students)

# 1️⃣ Number Frequency Counter
# Takes a list of integers.
# Uses a loop to count how many times each number appears.
# Stores the result in a dictionary.
# Prints the dictionary.
# Example Input:
# [1, 2, 2, 3, 1, 4, 2]

# numbers = [1, 2, 2, 3, 1, 4, 2]
# frequency = {}
# for num in numbers:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1
# print(frequency)

# # 2️⃣ Reverse Words in a Sentence
# # Takes a sentence (string input).
# # Uses a loop to reverse each word individually.
# # Prints the modified sentence.
# # Example Input:
# # "hello world"

# sentence = "hello world"
# words = sentence.split()
# reversed_sentence = ""
# for word in words:
#     reversed_word = ""
#     for char in word:
#         reversed_word = char + reversed_word
#     reversed_sentence += reversed_word + " "
# print(reversed_sentence.strip())

# # 3️⃣ Find Prime Numbers in a Range
# # Takes two integers as a range (start and end).
# # Uses nested loops to find all prime numbers in that range.
# # Stores the primes in a list.
# # Prints the list.
# # Example Input:
# # Start: 10
# # End: 20

# start = 10
# end = 20
# primes = []
# for num in range(start, end + 1):
#     if num > 1:
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
# print(primes)

# 4️⃣ Character Occurrence Counter
# Takes a string.
# Uses a loop to count how many times each character appears.
# Ignores spaces.
# Stores results in a dictionary.
# Example Input:
# "apple"

# text ="apple"
# char_count={}
# for char in text:
#     if char!= " ":
#         if char in char_count:
#             char_count[char] +=1
#         else:
#             char_count[char]=1
# print(char_count)

# 5️⃣ Sum of Even Numbers in Nested List
# Takes a nested list of integers (e.g., [[1,2,3], [4,5], [6]]).
# Uses nested loops to find the sum of all even numbers.
# Prints the total sum.
# Example Input:
# [[1,2,3], [4,5], [6]]

# nested_list=[[1, 2, 3],[4, 5],[6]]
# total=0
# for sublist in nested_list:
#     for num in sublist:
#         if num%2 ==0:
#             total +=num
# print(total)


# 1. Functions – Problem Solving
# Variable-Length Arguments
# Write a function find_max(*args) that returns the maximum value from any number of inputs.

# def find_max(*args):
#     if not args:
#         return None
#     maximum = args[0]
#     for num in args:
#         if num > maximum:
#             maximum = num
#     return maximum
# print(find_max(3, 7, 2, 9))

# Function Returning Multiple Values
# Write a function analyze_numbers(numbers) that returns:
# Sum
# Average
# Maximum
# Minimum

# def analyze_numbers(numbers):
#     total = sum(numbers)
#     average = total / len(numbers)
#     maximum = max(numbers)
#     minimum = min(numbers)
#     return total, average, maximum, minimum
# nums = [10, 20, 30, 40, 50]
# total, avg, max_val, min_val = analyze_numbers(nums)
# print("Sum:", total)
# print("Average:", avg)
# print("Maximum:", max_val)
# print("Minimum:", min_val)

# Recursive Problem
# Write a recursive function to calculate:
# Sum of digits of a number
# GCD of two numbers

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
# print(gcd(48, 18))

# Higher-Order Function
# Write a function apply_operation(func, a, b) that applies a function passed as argument to a and b.

# def apply_operation(func, a, b):
#     return func(a, b)
# def add(x, y):
#     return x + y
# print(apply_operation(add, 5, 3))

# 2. Lambda Functions – Problem Solving
# Sort Using Lambda
# Sort a list of tuples based on:
# Second element
# Last character of string

# data = [(1, 3), (4, 1), (2, 2)]
# sorted_data = sorted(data, key=lambda x: x[1])
# print(sorted_data)

# Filter with Lambda
# Given a list of numbers:
# Filter even numbers
# Filter prime numbers

# nums = [1, 2, 3, 4, 5, 6]
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)

# Map with Lambda
# Given a list of temperatures in Celsius, convert them to Fahrenheit.

# temps = [0, 20, 30]
# fahrenheit = list(map(lambda c: (c * 9/5) + 32, temps))
# print(fahrenheit)

# Reduce with Lambda
# Find the product of all elements in a list using reduce().

# from functools import reduce
# nums = [1, 2, 3, 4]
# product = reduce(lambda x, y: x * y, nums)
# print(product)

# 3. Importing & Creating Modules
# Create a Custom Module
# Create a module named math_utils.py containing:
# add(a, b)
# subtract(a, b)
# is_prime(n)
# Import it in another file and use the functions.
# # math_utils.py

# def add(a, b):
#     return a + b
# def subtract(a, b):
#     return a - b
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# 4. Datetime Module Problems
# Current Date & Time
# Write a program that prints:
# Current date
# Current time
# Current year

# from datetime import datetime
# now = datetime.now()
# print("Date:", now.date())
# print("Time:", now.time())
# print("Year:", now.year)

# Age Calculator
# Write a function that calculates age from date of birth.

# from datetime import date
# def calculate_age(year, month, day):
#     today = date.today()
#     birth = date(year, month, day)
#     age = today.year - birth.year
#     if (today.month, today.day) < (birth.month, birth.day):
#         age -= 1
#     return age
# print(calculate_age(2000, 5, 10))

# Countdown Timer
# Write a function that calculates how many days are left until New Year.

# from datetime import date
# def days_until_new_year():
#     today = date.today()
#     new_year = date(today.year + 1, 1, 1)
#     delta = new_year - today
#     return delta.days
# print("Days until New Year:", days_until_new_year())

# 🔴 5. Exception Handling Problems
# 2️⃣0️⃣ Basic Try-Except
# Write a function that divides two numbers and handles:
# Division by zero
# Invalid input

# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Cannot divide by zero"
#     except TypeError:
#         return "Invalid input"
# print(divide(10, 0))

# Custom Exception
# Create a custom exception InvalidAgeError:
# Raise it if age < 18
# Handle it properly

# class InvalidAgeError(Exception):
#     pass
# def check_age(age):
#     if age < 18:
#         raise InvalidAgeError("Age must be 18 or above")
#     return "Eligible"
# try:
#     print(check_age(16))
# except InvalidAgeError as e:
#     print(e)

# 🟠 6. OOP Concepts – Interview Problems
# 🔹 Class & Object
# Student Class
# Create a class Student with:
# Name
# Marks
# Method to calculate grade

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def grade(self):
#         if self.marks >= 90:
#             return "A"
#         elif self.marks >= 75:
#             return "B"
#         else:
#             return "C"
# s1 = Student("John", 85)
# print(s1.grade())

# 🔹 Inheritance
# Shape Class
# Create a base class Shape:
# Method area()
# Create derived classes:
# Circle
# Rectangle
# Override area method.

# import math
# class Shape:
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius ** 2
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
# c = Circle(5)
# r = Rectangle(4, 6)
# print(c.area())
# print(r.area())

# 🔹 Polymorphism
# Animal Sounds
# Create classes:
# Dog
# Cat
# Cow
# Each with method sound()
# Call them using same interface.
# Base concept: Same method name, different behavior

# class Dog:
#     def sound(self):
#         return "Dog says: Bark"
# class Cat:
#     def sound(self):
#         return "Cat says: Meow"
# class Cow:
#     def sound(self):
#         return "Cow says: Moo"
# animals = [Dog(), Cat(), Cow()]
# for animal in animals:
#     print(animal.sound())

# 🔹 Encapsulation
# Employee Class
# Create class with:
# Private salary variable
# Getter and setter methods

# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary
#     def get_salary(self):
#         return self.__salary
#     def set_salary(self, amount):
#         if amount > 0:
#             self.__salary = amount
# emp = Employee(50000)
# emp.set_salary(60000)
# print(emp.get_salary())

# 🔹 Abstraction
# Abstract Class
# Create abstract class Vehicle with:
# Abstract method start()
# Create subclasses:
# Car
# Bike

# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     def start(self):
#         pass
# class Car(Vehicle):
#     def start(self):
#         return "Car starts with a key or push button."
# class Bike(Vehicle):
#     def start(self):
#         return "Bike starts with a self-start or kick."
# car = Car()
# bike = Bike()
# print(car.start())
# print(bike.start())