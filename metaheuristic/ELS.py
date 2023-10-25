import numpy as np
import sys
sys.path.append('./intensification')
from Insertion_Backward_First_Improvement import IBFI
from methods import feasible, time_Z
from time import time
import random


def ELS(sol, Z, nit, nc, timep, order, jobs, machines, time_limit):
    t1 = time()
    sol, Z = IBFI(sol, Z, timep, order, jobs, machines)
    for _ in range(nit):
        sol2 = []; Z2 = np.float('inf')
        for _ in range(nc):
            sol3, Z3 = perturbation(np.copy(sol), np.copy(Z), timep, order, jobs, machines)
            sol3, Z3 = IBFI(sol3, Z3, timep, order, jobs, machines)
            if Z3 < Z2:
                sol2 = np.copy(sol3); Z2 = np.copy(Z3)
            t2 = time()
            if t2 - t1 > time_limit:
                break
        if Z2 < Z:
            sol = np.copy(sol2); Z = np.copy(Z2)
        if t2 - t1 > time_limit:
                break
    return sol, Z


def perturbation(sol, Z, timep, order, jobs, machines):
    while True:
        m = random.randrange(machines)
        i = random.randrange(1,jobs)
        # j = random.randrange(jobs)
        # while i == j:
            # j = random.randrange(jobs)
        sol[m][i-1], sol[m][i] = sol[m][i], sol[m][i-1]
        #print("Pert")
        if feasible(sol, order, jobs, machines):
            # print("FEASIBLE")
            Z = time_Z(sol, timep, order, jobs, machines)
            return sol, Z