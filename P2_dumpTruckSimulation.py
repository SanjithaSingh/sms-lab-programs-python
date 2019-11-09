# 
#   P2_dumpTruckSimulation.py
#   Dump Truck Problem simulation
#
#   Created by Mohammed Ataa on 9/11/19.
#   Copyright © 2019 Ataago. All rights reserved.
#   
#   Write a program to simulate the multi-channel dump truck system consisting of 6 trucks, 2 loaders and 1 scale. 
#   Consider the standard initial assumptions. Calculate the server utilizations for a simulation period of 72 minutes
#

from random import randint

class Event:
    """ Individual Events can be described

        name: 
            Event Names are as follows for this simulation
                END:    End of Simulation Time
                EL:     End of Loading Time
                EW:     End of Weighing Time
                ET:     End of Travel Time
        time: 
            Clock time of the Event when it occurs
        truck:
            The Dump Truck Number
    """
    def __init__(self, name, time, truck):
        self.name = name
        self.time = time
        self.truck = truck

    def displayEvent(self):
        print('\t\t(',self.name, ', ',self.time, ', ',self.truck, ')')


class FutureEventList:
    """ Future Event List consists of all the events which will occur in the Future """
    def __init__(self):
        self.events = []
    
    def addEvent(self, newEvent):
        """ Helps to add the Event in the Future Event List in a sorted manner """
        index = 0
        for event in self.events:
            if newEvent.time > event.time:
                index += 1
        self.events.insert(index, newEvent)
    
    def removeEvent(self):
        """ Returns the First Event which is having the least time as its sorted FEL """
        event = self.events[0]
        self.events.pop(0)
        return event

    def displayFEL(self):
        for event in self.events:
            event.displayEvent()


class simulationState:
    """ Stores data for the various Parameters of the Simulation in its States
            lq: Loader Queue list
            l : Number of Trucks in 2 loading servers 
            wq: Weighing Queue list
            w : Number of Trucks in 1 Weighing Server
            fel: Future Event List
    """
    def __init__(self, lq, l, wq, w, fel):
        self.clk = 0        # Clock time of the Simulation State
        self.lq = lq        # list of Dump trucks in Loading Queue
        self.l = l          # number of Dump trucks in Loading Server
        self.wq = wq        # list of Dump trucks in Weighing Queue
        self.w = w          # number of Dump trucks in Weighing Server
        self.fel = fel      # Future Event List


def workTIme(clk, a, b):
    return clk + randint(a, b)

def printState(state):
    print('\n\n--------------------------------------\nCLK: ', state.clk, '\n--------------------------------------')
    print('Loader Queue (lq)\t\t: ', state.lq)
    print('Trucks in Loader Server (l)\t: ', state.l)
    print('Weighing Queue (wq)\t\t: ', state.wq)
    print('Trucks in Weighing Server (w)\t: ', state.w)
    print('FEL:')
    state.fel.displayFEL()

def simulate(state):
    printState(state)
    curEvent = state.fel.removeEvent()  # Capture the Curent Event From The Future Event List
    state.clk = curEvent.time   # Update simulation Clock

    # Event When Loading Ends at the server
    if curEvent.name == 'EL':
        state.l -= 1
        if state.w == 0:     # Weighing server and weighing Queue is free
            state.w = 1
            state.fel.addEvent(Event('EW', workTIme(state.clk, 10, 30), curEvent.truck))
        else:
            state.wq.append(curEvent.truck)
        
        if state.lq: # Loading Queue has Dump Trucks then push it in the server
            truck = state.lq.pop(0)
            state.l += 1
            state.fel.addEvent(Event('EL', workTIme(state.clk, 10, 20), truck))

    # Event when Weighing Ends at the Server
    if curEvent.name == 'EW':
        if state.wq: # If trucks are waiting in the weighing queue
            truck = state.wq.pop(0)
            state.fel.addEvent(Event('EW', workTIme(state.clk, 10, 30), truck))
        else:
            state.w -= 1
        
        state.fel.addEvent(Event('ET', workTIme(state.clk, 50, 100), curEvent.truck))
    
    # Event When Truck Arives Back to the Server
    if curEvent.name == 'ET':
        if state.l <= 1:  # Atleast 1 load server is free
            state.l += 1
            state.fel.addEvent(Event('EL', workTIme(state.clk, 10, 20), curEvent.truck))
        else:
            state.lq.append(curEvent.truck)
    
    # End of Simulation Time
    if curEvent.name == 'END':
        printState(state)
        return
        
    simulate(state)


if __name__ == '__main__':

    fel = FutureEventList()     # Intializing an Empty Future Event List
    lq = []     # Dump Trucks in Loading Queue
    wq = []     # Dump Trucks in Weighing Queue

    # End of stateulation Time added to FEL
    fel.addEvent(Event('END', 15, 0))      # 100 is the End of Simulation time

    # States of Dump Trucks Initialy
    fel.addEvent(Event('EW', 12, 1))    # DT1
    fel.addEvent(Event('EL', 10, 2))    # DT2
    fel.addEvent(Event('EL', 5, 3))     # DT3
    lq.append(4)                        # DT4
    lq.append(5)                        # DT5
    lq.append(6)                        # DT6

    # Dump trucks state at CLK = 0
    state = simulationState(lq, 2, wq, 1, fel)

    simulate(state)