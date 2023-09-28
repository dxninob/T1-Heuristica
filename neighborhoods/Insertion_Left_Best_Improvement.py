import numpy as np
from methods import feasible, time_Z
import time

def ILBI(sol, Z, timep, order, jobs, machines):
    sol_neighbor = []
    Z_neighbor = Z
    stop = False
    while not stop:
        stop = True
        for m in range(machines):
            for j in range(jobs):
                for i in range(j-1, -1, -1):
                    sol_neighbor_temp = move(sol, m, j, i)
                    if feasible(sol_neighbor_temp, order, jobs, machines):
                        Z_neighbor_temp = time_Z(sol_neighbor_temp, timep, order, jobs, machines)
                        if Z_neighbor_temp < Z_neighbor:
                            stop = False
                            sol_neighbor = sol_neighbor_temp # Es necesario hacer la copia?
                            Z_neighbor = Z_neighbor_temp
                    else:
                        break
        if not stop:
            sol = sol_neighbor # Es necesario hacer la copia?
            Z = Z_neighbor
    return sol, Z


def move(sol, m, j, i):
    new_sol = np.copy(sol)
    for k in range(j-1,i-1,-1):
        new_sol[m][k+1] = new_sol[m][k]
    new_sol[m][i] = sol[m][j]
    return new_sol