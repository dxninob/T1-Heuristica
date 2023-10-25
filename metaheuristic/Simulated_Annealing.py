import numpy as np
import sys
sys.path.append('./intensification')
from Insertion_Forward_First_Improvement import IFFI
from time import time
from random import random
from math import exp


def Simulated_Annealing(sol, Z, T0, Tf, L, p, timep, order, jobs, machines, time_limit):
    t1 = time(); t2 = time(); current_time = t2 - t1
    sol1 = sol
    Z1 = Z
    while current_time < time_limit:
        T = T0
        while T > Tf:
            l = 0
            while l < L and current_time < time_limit:
                l += 1
                sol2, Z2 = IFFI(sol, Z, timep, order, jobs, machines)
                if Z2 < Z:
                    sol = sol2; Z = Z2
                    if Z < Z1:
                        sol1 = sol; Z1 = Z
                else:
                    r = random()
                    if r < exp(-(Z2 - Z)/T):
                        sol = sol2; Z = Z2
                t2 = time()
                current_time = t2 - t1
            T = p*T
            if current_time >= time_limit:
                break

    return sol1, Z1