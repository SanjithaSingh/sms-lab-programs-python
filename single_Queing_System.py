# 
#   single_Queing_System.py
#   Single Server Queue Simulation
#
#   Created by Mohammed Ataa on 2/11/19.
#   Copyright © 2019 Ataago. All rights reserved.
#   

import numpy as np


# Number of Customers
# n = int(input("Enter Number of Customers to Simulate Single Server Queue: "))
n = 10
interArrivalTimeRange = [1, 2, 3, 4, 5, 6, 7, 8]  # Arrival time distributed from 1 to 8 mins
probArivalTime = [1/8] * 8  # Equal Probalitiy for each Arival time
RDArival = np.random.randint(0, 100, n)

serviceTimeRange = [1, 2, 3, 4, 5, 6]    # Service Time Distributed across 1 to 6 mins
probServiceTime = [0.10, 0.20, 0.30, 0.25, 0.10, 0.05]
RDService = np.random.randint(0, 100, n)

# Finding The Random Digit Ranges for Arival Time
RDRangeArival = []
for i in range(len(probArivalTime)):
    RDRangeArival.append(sum(probArivalTime[0:i + 1]) * 100)

# Finding Inter Arival Time and Cumulative time for Each Customer
InterArivalTimeCustomer = [0, ]
cumArivalTime = []
for i in range(n):
    for j in range(len(interArrivalTimeRange)):
        if RDArival[i] <= RDRangeArival[j]:
            InterArivalTimeCustomer.append(interArrivalTimeRange[j])
            break
    cumArivalTime.append(sum(InterArivalTimeCustomer[0:i + 1]))

# Finding RD Range for Service Time
RDRangeService = []
for i in range(len(probServiceTime)):
    RDRangeService.append(sum(probServiceTime[0:i + 1]) * 100)

# Finding the Service Time for each Customer
serviceTimeCustomer = []
for i in range(n):
    for j in range(len(serviceTimeRange)):
        if RDService[i] <= RDRangeService[j]:
            serviceTimeCustomer.append(serviceTimeRange[j])
            break

print(RDRangeArival)
print(RDArival)
print(InterArivalTimeCustomer)
print(cumArivalTime)

print()
print(RDService)
print(RDRangeService)
print(serviceTimeCustomer)

# Tabulating the Table for each customer for TSB, TSE, WT, and IT
TSB = []
TSE = []
WT, IT = [], []
for i in range(n):   # Iterating over each customer 1, 2, 3, .. n
    if i == 0:
        TSB.append(cumArivalTime[i])
        TSE.append(serviceTimeCustomer[i])
        break
    
    WT.append(TSB - )
