import simpy
import itertools
import random
import statistics



class CCSC(object):
    def __init__(self, env, num_beds):
        self.env = env
        self.bed = simpy.Resource(env, 4)

    def colonoscopy(self, patient):
        yield self.env.timeout(random.randint(30,75))

def have_a_scope(env, patient, ccsc):
   with ccsc.bed.request() as request:
        yield request
        print(f'{patient} arrives at CCSC {env.now:.2f}.')
        yield env.process(ccsc.colonoscopy(patient))
        print(f'{patient} leaves CCSC {env.now:.2f}.')

def perform_scopes(env, num_beds):
    c_csc = CCSC(env, num_beds)
    patients = itertools.count()

    for patient in range(1):
        env.process(have_a_scope(env, f' patient {next(patients)}', c_csc))

    while True:
        yield env.timeout(30)
        env.process(have_a_scope(env, f' patient {next(patients)}', c_csc))

env = simpy.Environment()
env.process(perform_scopes(env, 4))
env.run(until=300)