import numpy as np
import sys
sys.path.append('./algorithms')
from algorithm2 import noise
sys.path.append('./intensification')
from Insertion_Forward_First_Improvement import IFFI
from Simulated_Annealing import Simulated_Annealing
from ELS import ELS


def Mixed(nsol, T0, Tf, L, p, nit, nc, r, jobs, machines, timep, order, time_limit):
    time_limit = time_limit/4
    best_sol = []; best_Z = np.float('inf')
    n = 0
    while n < nsol:
        sol, Z = noise(jobs,machines,timep,order,r)
        sol, Z = IFFI(sol, Z, timep, order, jobs, machines)
        sol, Z = Simulated_Annealing(sol, Z, T0, Tf, L, p, timep, order, jobs, machines, time_limit)
        if Z < best_Z:
            best_sol = sol; best_Z = Z
        n += 1

    best_sol, best_Z = ELS(best_sol, best_Z, nit, nc, timep, order, jobs, machines, time_limit)
    return best_sol, best_Z
