# 
#   P4_chiSquareTest.py
#   C
hi Square Test
#
#   Created by Sanjitha Singh on 2/11/19.
#   Copyright © 2019 SanjithaSingh. All rights reserved.
# 
#   Write a program to show goodness of fit test using Chi-Square Test 
#   for the input set of random numbers. Assume significance value is equal to 0.05. 
#   Dcritical = 16.9
#
from random import random


def input_random_numbers():
    random_numbers = input("Enter the random numbers: ")
    random_numbers = [float(i) for i in random_numbers.split()]
    return random_numbers


def generate_random_numbers(n): #optional
    random_numbers = [round(random(), 4) for i in
                      range(n)]  # n random numbers generated between 0 to 1 rounded to 4 digits
    print("Generated Random numbers:", random_numbers)
    return random_numbers


random_numbers = input_random_numbers()
# random_numbers=generate_random_numbers(20)
n = int(input("Enter the number of class intervals: "))

# generating upper-bound of ranges
ranges = []
interval = 1 / n
for i in range(1, n + 1):
    ranges.append(interval * i)

# calculating frequencies for observed values (Oi)
frequency = [0] * n
for i in random_numbers:
    for j in range(n):
        if i <= ranges[j]:
            frequency[j] += 1
            break

# Calculating expected value Ei
N = len(random_numbers)
expected_value = N / n

# Calculating ((Oi-Ei)^2)/Ei
summation = 0
summation_array = []
for o in frequency:
    result = ((o - expected_value) ** 2) / expected_value
    summation += result
    summation_array.append(result)

# display the calculation table
print("Class(n)\tOi\tEi\t(Oi-Ei)^2/Ei")
print("-" * 30)
for i in range(n):
    print("\t{}\t\t{}\t{}\t{}".format((i + 1), frequency[i], expected_value, summation_array[i]))

print("Summation: ", summation)

# Check if the null hypothesis is accepted or not
dcritical = float(input("Enter the D-Critical Value: "))
if summation < dcritical:
    print("Null hypothesis is accepted")
else:
    print("Null Hypothesis is rejected")
