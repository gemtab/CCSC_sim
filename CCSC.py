import simpy
import pandas 
import matplotlib
from random import choices
#developing the ability to model the function of the colon cancer screening centre

#To do:
#Develop the functions to: assign probability, define each resource, define each outcome, determine what I want to 
# measure and report

def time_multiplier(bottom_range, top_range):
    times = list(range(bottom_range, top_range + 1))
    return(times)

x= time_multiplier(1,5)
print(x)