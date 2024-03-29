import simpy
import pandas 
import matplotlib
from random import choices
#developing the ability to model the function of the colon cancer screening centre

#To do:
#Develop the functions to: assign probability, define each resource, define each outcome, determine what I want to 
# measure and report
def odd_list(lst):
    if len(lst) %2 != 0:
        lst.pop|(0)

def buckets (lst):
#median +/- 1 - should be 0.68/3, down to bottom would be rest of -1 to -3. Positive from median to end of list - x4 would 4, 2 would be 3, 1.5 would be 2
# and median to end of list would be +1



def time_multiplier(bottom_range, top_range):
    times = list(range(bottom_range, top_range + 1))
    times.extend([top_range *1.5, top_range *2, top_range *4])
    median_time = times.index(len(list) //2)
    
    return(times)

x = time_multiplier(5,10)
print(x)