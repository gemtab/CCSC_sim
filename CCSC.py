import simpy
import itertools
import random
import pandas as pd

patients = {}

class CCSC:
    def __init__(self, env, num_beds, name):
        self.env = env
        self.bed = simpy.Resource(env, 4)
        self.scope_room = simpy.Resource(env, 1)
        self.name = name
    def recovery(self, patient):
        yield self.env.timeout(random.randint(30,90))
    def scope(self, patient):
        yield self.env.timeout(random.randint(45,60))

def have_a_scope(env, patient, ccsc):
    with ccsc.bed.request() as bed_request:
        arrival_time = env.now
        print(f'{patient} arrives at CCSC {env.now:.2f}.')
        yield bed_request
        bed_time = env.now
        print(f'{patient} gets a bed for {ccsc.name} {env.now:.2f}.')

        with ccsc.scope_room.request() as scope_rm_request:
            yield scope_rm_request
            scope_time = env.now
            print(f'{patient} scope starts for {ccsc.name} {env.now:.2f}.')
            yield env.process(ccsc.scope(patient))

        scope_end = env.now
        print(f'{patient} scope ends for {ccsc.name} {env.now:.2f}.')
        yield env.process(ccsc.recovery(patient))

        departure_time = env.now
        print(f'{patient} leaves CCSC {env.now:.2f}.')

    patients[patient] = {"arrival time":arrival_time, "bed time":bed_time,"scope time": scope_time, "scope end": scope_end, "departure time":departure_time, "rm":ccsc.name }
def perform_scopes(env, num_beds, num_pats):
    room_list = []
    for i in range(1):
        room_list.append(CCSC(env, num_beds, "rm"+str(i)))
    #rm1 = CCSC(env, num_beds, "rm1")
    #rm2 = CCSC(env, num_beds, "rm2")
    print(room_list)
    #room_list = [rm1, rm2]

    patients = itertools.count()


    for room in room_list:
        env.process(have_a_scope(env, f'patient {next(patients)}',room))


    while True:
        #print('here i am')
        yield env.timeout(30)

        for room in room_list:
            env.process(have_a_scope(env, f'patient {next(patients)}',room))

env = simpy.Environment()
scope_iterator = perform_scopes(env, num_beds = 4,num_pats = 5)
env.process(scope_iterator)
#for i in range(5):
#    print(next(scope_iterator))
env.run(until=1000)
#print(patients)

df = pd.DataFrame(patients).T
print(df)