# 
#   single_Queing_System.py
#   Single Server Queue Simulation
#
#   Created by Mohammed Ataa on 2/11/19.
#   Copyright © 2019 Ataago. All rights reserved.
#   

from random import random

# Number of Customers
n = int(input("\nEnter Number of Customers to Simulate Single Server Queue: "))

IATRange = [1, 2, 3, 4, 5, 6, 7, 8]  # InterArrival time distributed from 1 to 8 mins
probIAT = [1/8] * 8  # Equal Probalitiy for each Arival time
RD_IAT = [round(random()*100) for i in range(n)]

STRange = [1, 2, 3, 4, 5, 6]    # Service Time Distributed across 1 to 6 mins
probST = [0.10, 0.20, 0.30, 0.25, 0.10, 0.05]
RD_ST = [round(random()*100) for i in range(n)]


#   To find IAT from Given Random Digits

    # IATRange        probIAT RDRangeIAT
    # -----------------------------------------
    # 1        0.125   12.5
    # 2        0.125   25.0
    # 3        0.125   37.5
    # 4        0.125   50.0
    # 5        0.125   62.5
    # 6        0.125   75.0
    # 7        0.125   87.5
    # 8        0.125   100.0

# Finding The Random Digit Ranges for Arival Time
RDRangeIAT = []
for i in range(len(IATRange)):
    RDRangeIAT.append(sum(probIAT[0:i + 1]) * 100)

# Finding Inter Arival Time and Cumulative time for Each Customer
IAT, AT = [0, ], []

for i in range(n):
    for j in range(len(IATRange)):
        if RD_IAT[i] <= RDRangeIAT[j]:
            IAT.append(IATRange[j])
            break
    AT.append(sum(IAT[0:i + 1]))

#   Printing RD Range Table
print('\nIATRange\tprobIAT\tRDRangeIAT\n-----------------------------------------')
for i in range(len(IATRange)):
    print(IATRange[i], '\t\t', probIAT[i], '\t', RDRangeIAT[i])
print('\nGiven RD: ', RD_IAT)
print('IAT:       ', IAT)

#   To find ST from Given Random Digits

        # STRange probST  RDRangeST
        # -----------------------------------------
        # 1        0.1     10.0
        # 2        0.2     30.000000000000004
        # 3        0.3     60.00000000000001
        # 4        0.25    85.00000000000001
        # 5        0.1     95.0
        # 6        0.05    100.0

# Finding RD Range for Service Time
RDRangeST = []
for i in range(len(STRange)):
    RDRangeST.append(sum(probST[0: i + 1]) * 100)

# Finding the Service Time for each Customer
ST = []
for i in range(n):
    for j in range(len(STRange)):
        if RD_ST[i] <= RDRangeST[j]:
            ST.append(STRange[j])
            break

#   Printing RD Range Table
print('\n\nSTRange\tprobST\tRDRangeST\n-----------------------------------------')
for i in range(len(STRange)):
    print(STRange[i], '\t', probST[i], '\t', RDRangeST[i])
print('\nGiven RD: ', RD_ST)
print('ST:       ', ST)


#  Table :
#
        # IAT     AT      ST      TSB     TSE     WT      IT
        # -----------------------------------------------------
        # 0        0       4       0       4       0       0
        # 1        1       4       4       8       3       0
        # 2        3       5       8       13      5       0
        # 3        6       4       13      17      7       0
        # 2        8       1       17      18      9       0
#
#           WT = TSB[i] - AT[i]
#           IT = TSB[i] - TSE[i - 1]
#
# Tabulating the Table for each customer for TSB, TSE, WT, and IT
TSB, TSE, WT, IT = [], [], [], []

for i in range(n):   # Iterating over each customer 1, 2, 3, .. n
    # First Customer
    if i == 0:
        TSB.append(AT[i])
        TSE.append(ST[i])
        WT.append(0)
        IT.append(0)
        continue

    # Customer Arrives when Server is Idle
    if AT[i] > TSE[i - 1]: 
        TSB.append(AT[i])
        TSE.append(TSB[i] + ST[i])
        WT.append(0)
        IT.append(TSB[i] - TSE[i - 1])
        continue

    # Customer arrives when server is Busy or just completed i.e AT[i] <= TSE[i - 1]
    TSB.append(TSE[i - 1])
    TSE.append(TSB[i] + ST[i])
    WT.append(TSB[i] - AT[i])
    IT.append(0)

# Printing The Table
print("\nIAT\tAT\tST\tTSB\tTSE\tWT\tIT\n-----------------------------------------------------")
for i in range(n):
    print(IAT[i], '\t', AT[i], '\t', ST[i], '\t', TSB[i], '\t', TSE[i], '\t', WT[i], '\t', IT[i])

def count_non_zeros(myList):
    return len(list(filter(lambda x: x != 0, myList)))
# Calculating the Metrics
wCount = count_non_zeros(WT)    # Number of Customers who Waited
iCount = count_non_zeros(IT)    # Number of Times the Server went to Idle States

print('\nAverage Service Time: ', sum(ST)/n)
print('Average Waiting Time of the Customers: ', sum(WT)/n)
if wCount != 0:
    print('Average Waiting TIme of the Customers who waited: ', sum(WT)/wCount)
print('Probablity of Waiting: ', wCount/n)
print('Average Time Spent by the Customers in the System: ', (sum(ST) + sum(WT))/n)
print('Probablity of Server going to Idle State: ', iCount/n)