# Exercises XP Ninja

# Exercise 1: Formula
# 1.Write a program that calculates and prints a value according to this given formula: Q = Square root of [(2 * C * D)/H]

# 2.Following are the fixed values of C and H:
# • C is 50.
# • H is 30.
# 3.Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
import math


acceptional_input = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',']
while True:
    usr_nums = input(
        'Please indicate the numbers you would like to calculate, seperate each number by a comma when complete hit enter: ')
    if any(char not in acceptional_input for char in usr_nums):
        continue
    break
nums_to_calculate = list(usr_nums.split(","))
nums_to_calculate_int = map(int, nums_to_calculate)

sqr_roots_lst = []
q = 0
for n in nums_to_calculate_int:
    q = 0
    q = math.sqrt((2 * 50 * n)/30)
    sqr_roots_lst.append(int(q))

print(sqr_roots_lst)


# Exercise 2 : List Of Integers
# Given a list of 10 integers to analyze. For example:
# 1.Store the list of numbers in a variable.
lst_one = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7, 44, 91, 8, 24, -6, 0, 56, 8, 100,
           2, 3, 21, 76, 53, 9, -82, -3, 49, 1, 76, 18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# 2.Print the following information:
# a.The list of numbers – printed in a single line
print(lst_one)
