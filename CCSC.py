import simpy
import pandas 
import matplotlib
import random
#developing the ability to model the function of the colon cancer screening centre

#To do:
#Develop the functions to: assign probability, define each resource, define each outcome, determine what I want to 
# measure and report


#median +/- 1 - should be 0.68/3, down to bottom would be rest of -1 to -3. Positive from median to end of list - x4 would 4, 2 would be 3, 1.5 would be 2
# and median to end of list would be +1
# bottom_range to median should 2 sigma, median to top should be 4 sigma. 

# random.choices(population, weights=None, *, k=1)
#print(random.choices(numberList, weights=(10, 20, 30, 40, 50), k=5))

def scope_time_multiplier (bottom_range, top_range):
    times = list(range(bottom_range, top_range + 1))

    times2 = times + [int(top_range *1.5), int(top_range *2), int(top_range *4)]
    median_index = (len(times2)//2) -2
    median_term = times2[median_index]
    next_term = median_index + 1
    previous_term = median_index - 1

    Count_Below_Median = len(times2[:median_index])
    Count_Above_Median = len(times2[median_index:])
    
    weights = [0.002,0.002,0.002,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.002,0.001]
    time = random.choices(times2, weights = weights, k = 1)
    return time

x = scope_time_multiplier(15,30)
print(x)