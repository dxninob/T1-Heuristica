import sys
sys.path.append('./algorithms')
from algorithm2 import noise
sys.path.append('./intensification')
from methods import feasible, time_Z
from Insertion_Forward_First_Improvement import IFFI
sys.path.append('./metaheuristic')
from VND import VND
from time import time
from random import sample, random, randint, choice
import numpy as np


def GA(nsol, nc, prob_muta, prob_LS, r_noise, jobs, machines, timep, order, time_limit):
    time_limit_VND = time_limit*0.1

    P_sol = [[] for _ in range(nsol)]; P_Z = [0 for _ in range(nsol)]
    for i in range(nsol):
        sol, Z = noise(jobs,machines,timep,order,r_noise)
        P_sol[i] = sol; P_Z[i] = Z

    t1 = time(); current_time = 0
    while current_time < time_limit:
        c_sol = [[] for _ in range(nc)]; c_Z = [0 for _ in range(nc)]
        for i in range(nc):
            p1, p2, a, b = selection(P_sol, P_Z, nsol)
            H = crossover(p1, p2, order, jobs, machines, 0)
            r = random()
            if r < prob_muta:
                H = mutation(sol, order, jobs, machines)
                Z = time_Z(H, timep, order, jobs, machines)
            elif r < prob_LS:
                H, Z = IFFI(sol, Z, timep, order, jobs, machines)

            c_sol[i] = H; c_Z[i] = time_Z(H, timep, order, jobs, machines)

        P_sol, P_Z = update(P_sol, P_Z, c_sol, c_Z, a, b)
        t2 = time(); current_time = t2 - t1

    pos = P_Z.index(min(P_Z))
    return P_sol[pos], P_Z[pos]


def selection(P_sol, P_Z, nsol):
    total = np.sum(P_Z)
    prob = total/P_Z
    total = np.sum(prob)
    prob /= total
    a = np.random.choice(range(nsol), p=prob)
    b = np.random.choice(range(nsol), p=prob)
    while a == b:
        b = np.random.choice(range(nsol), p=prob)
    return P_sol[a], P_sol[b], a, b


def crossover(p1, p2, order, jobs, machines, iter):
    r = randint(1, machines-2)
    H1 = np.concatenate((p1[:r], p2[r:]))
    H2 = np.concatenate((p2[:r], p1[r:]))

    H1_f = feasible(H1, order, jobs, machines)
    H2_f = feasible(H2, order, jobs, machines)

    if H1_f and H2_f:
        return choice([H1, H2])
    elif H1_f:
        return H1
    elif H2_f:
        return H2
    else:
        return choice([p1, p2])
        # if iter < 10:
        #     crossover(p1, p2, order, jobs, machines, iter+1)
        # else:
        #     return choice([p1, p2])


def update(P_sol, P_Z, c_sol, c_Z, a, b):
    best_child = np.argmin(c_Z)
    if P_Z[a] < P_Z[b]:
        worse_parent = b
    else:
        worse_parent = a
    
    P_Z[worse_parent] = c_Z[best_child]
    P_sol[worse_parent] = c_sol[best_child]
    return P_sol, P_Z


def mutation(sol, order, jobs, machines):
    m = randint(0, machines-1)
    i = randint(0, jobs-1)
    j = randint(0, jobs-1)
    while i == j:
        j = randint(0, jobs-1)

    sol[m][i], sol[m][j] = sol[m][j], sol[m][i]
    if feasible(sol, order, jobs, machines):
        return sol
    else:
        sol[m][i], sol[m][j] = sol[m][j], sol[m][i]
        return sol