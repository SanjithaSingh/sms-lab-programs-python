# 
#   P5_autoCorrelationTest.py
#   Auto Correlation Test
#
#   Created by Sanjitha Singh on 2/11/19.
#   Copyright © 2019 SanjithaSingh. All rights reserved.
# 
#   Write a program to show goodness of fit test using Autocorrelation test for the input set of random numbers. 
#   Assume Zα/2=1.96
#

from math import floor, sqrt
from random import random


def input_random_numbers():
    random_numbers = input("Enter the random numbers: ")
    random_numbers = [float(i) for i in random_numbers.split()]
    return random_numbers


def generate_random_numbers(n): #optional
    random_numbers = [round(random(), 4) for i in range(n)]  # n random numbers generated between 0 to 1 rounded to 4 digits
    print("Generated Random numbers:", random_numbers)
    return random_numbers


R = input_random_numbers()
# random_numbers=generate_random_numbers(30)

i = int(input("Enter the start point(i): "))
m = int(input("Enter the gap(m): "))
N = len(R)

# calculate M where i+(M+1)m<=N
M = floor(((N - i) / m) - 1)

# calculate rho
rho = 0
for k in range(M + 1):
    rho += R[i + k * m] + R[i + (k + 1) * m]
rho = (rho / (M + 1)) - 0.25

# calculate sigma
sigma = sqrt(13 * M + 7) / 12 * (M + 1)

# calculate Z0
Z0 = rho / sigma

# display results
print("N: ", N)
print("M: ", M)
print("rho: ", rho)
print("sigma: ", sigma)
print("Z0: ", Z0)

# Check if the null hypothesis is accepted or not
zcritical = float(input("Enter the Z-Critical Value: "))
if Z0 < zcritical:
    print("Null hypothesis is accepted")
else:
    print("Null Hypothesis is rejected")
