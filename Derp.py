""" Scenario - patient arrives, is assigned a bed, is checked in for 5-10 minutes, has a scope in 
a scope room for 15min to 2 hours, recovers for 30-120 min and then leaves """
import simpy
#import pandas 
#import matplotlib
#import random
#developing the ability to model the function of the colon cancer screening centre

#To do:
#Develop the functions to: assign probability, define each resource, define each outcome, determine what I want to 
# measure and report


#median +/- 1 - should be 0.68/3, down to bottom would be rest of -1 to -3. Positive from median to end of list - x4 would 4, 2 would be 3, 1.5 would be 2
# and median to end of list would be +1
# bottom_range to median should 2 sigma, median to top should be 4 sigma. 

# random.choices(population, weights=None, *, k=1)
#print(random.choices(numberList, weights=(10, 20, 30, 40, 50), k=5))

# def scope_time_multiplier (bottom_range, top_range):
#     times = list(range(bottom_range, top_range + 1))

#     times2 = times + [int(top_range *1.5), int(top_range *2), int(top_range *4)]
#     median_index = (len(times2)//2) -2
#     median_term = times2[median_index]
#     next_term = median_index + 1
#     previous_term = median_index - 1

#     #Count_Below_Median = len(times2[:median_index])
#     #Count_Above_Median = len(times2[median_index:])
#     #future code for dynamically building probability distributions
    
#     weights = [0.002,0.002,0.002,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.002,0.001]
#     time = random.choices(times2, weights = weights, k = 1)
#     return time

###Simpy code to simulate the first 50 patients in five rooms.
#from https://simpy.readthedocs.io/en/latest/simpy_intro/shared_resources.html
# and https://simpy.readthedocs.io/en/latest/examples/carwash.html

num_beds = 4
num_rooms = 1
checkin = 10
recovery = 30
total_time = 40
sim_time = 200
t_inter = 30

class CCSC:
    def __init__(self, env, bed, totaltime):
        self.env = env
        self.bed = simpy.Resource(num_beds)
        self.totaltime = total_time
        #self.room = simpy.Resources(env, num_rooms)

    #def checkin(self, patient):
    #    yield self.env.timeout(self.checkin)
        
    def procedure(self, patient):
        yield self.env.timeout(self.totaltime)
        
    #def recovery(self, patient):    
    #    yield self.env.timeout(self.recovery)

def patient(env, name, c_c):
    print(f'{name} arrives at the CCSC at {env.now:.2f}.')
    with c_c.bed.request() as request:
        yield request

        print(f'{name} gets a bed at {env.now:.2f}.')
        yield env.process(c_c.procedure(name))

        print(f'{name} leaves CCSC at {env.now:.2f}.')

def setup(env, num_beds, total_time, t_inter):
    c_c_s_c = CCSC(env, num_beds, total_time)
    env.process(patient(env, patient, c_c_s_c))
    
    while True:
        yield env.timeout(t_inter)
        env.process(patient, c_c_s_c)

env = simpy.Environment()
env.process(setup(env, num_beds, total_time, t_inter))

env.run(until = sim_time)
