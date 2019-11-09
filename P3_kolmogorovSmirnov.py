# 
#   P3_kolmogorovSmirnov.py
#   Kolmogrov Smirnov Test
#
#   Created by Mohammed Ataa on 9/11/19.
#   Copyright © 2019 Ataago. All rights reserved.
#   
#   Write a program to show goodness of fit test using Kolmogorov Smirnov Test for 
#   the given population of random numbers. Assume significance value is equal to 0.05.
#   Dcritical = 0.565
#


# Enter the Random Numbers and store it in sorted format
Ri = sorted([float(i) for i in input("Enter Random numbers to perform Kolmogorov Smirnov Test: ").split()])

# Total Number of Random Digits
N = len(Ri)

# Calculating D+ and D- for Each Random Digit
# 
#   D+ = [i/N - Ri]
#   D- = [Ri - (i - 1)/N]
#       Where i ranges from 1 to N
Dplus, Dminus = [], []

for i in range(N):   # for i = 0 to N - 1
    Dplus.append(round((i + 1)/N - Ri[i], 2))
    Dminus.append(round((Ri[i] - i/N), 2))

Dmax = max(max(Dplus), max(Dminus))

# Printing the Table
print('\ni\tRi\tD+ = i/N-Ri\tD- = Ri-(i-1)/N\n--------------------------------------------------')
for i in range(N):
    print(i + 1, '\t', Ri[i], '\t',Dplus[i], '\t\t', Dminus[i])

print('\nD max : ', Dmax)
Dcritical = float(input("Enter D Critical Value: "))

if Dmax <= Dcritical:
    print('Hypothesis H0 is Accepted')
else:
    print('Hypothesis H0 is Rejected')