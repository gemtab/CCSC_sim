import simpy
import itertools
import random
import statistics



class CCSC:
    def __init__(self, env, num_beds):
        self.env = env
        self.bed = simpy.Resource(env, 4)

    def colonoscopy(self, patient):
        yield self.env.timeout(random.randint(30,75))

def have_a_scope(env, patient, ccsc):
    with ccsc.bed.request() as request:
        print(f'{patient} arrives at CCSC {env.now:.2f}.')
        yield request
        print(f'{patient} gets a bed at CCSC {env.now:.2f}.')
        yield env.process(ccsc.colonoscopy(patient))
        print(f'{patient} leaves CCSC {env.now:.2f}.')

def perform_scopes(env, num_beds, num_pats):
    c_csc = CCSC(env, num_beds)
    patients = itertools.count()

    for i in range(num_pats):
        env.process(have_a_scope(env, f' patient {next(patients)}', c_csc))

    while True:
        #print('here i am')
        yield env.timeout(30)
        for i in range(num_pats):
            env.process(have_a_scope(env, f' patient {next(patients)}', c_csc))

env = simpy.Environment()

scope_iterator = perform_scopes(env, num_beds = 4,num_pats = 1)
env.process(scope_iterator)
#for i in range(5):
#    print(next(scope_iterator))
#env.run(until=300)