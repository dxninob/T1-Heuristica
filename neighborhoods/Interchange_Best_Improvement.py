import numpy as np
from methods import feasible, time_Z


def IBI(sol, Z, timep, order, jobs, machines):
    sol_neighbor = []
    Z_neighbor = Z
    stop = False
    while not stop:
        stop = True
        for m in range(machines):
            for j in range(jobs):
                for i in range(j+1, jobs):
                    sol_neighbor_temp = move(sol, m, j, i)
                    if feasible(sol_neighbor_temp, order, jobs, machines):
                        Z_neighbor_temp = time_Z(sol_neighbor_temp, timep, order, jobs, machines)
                        if Z_neighbor_temp < Z_neighbor:
                            stop = False
                            sol_neighbor = sol_neighbor_temp # Es necesario hacer la copia?
                            Z_neighbor = Z_neighbor_temp
        if not stop:
            sol = np.copy(sol_neighbor) # Es necesario hacer la copia?
            Z = Z_neighbor
    return sol, Z


def move(sol, m, j, i):
    new_sol = np.copy(sol)
    new_sol[m][j], new_sol[m][i] = new_sol[m][i], new_sol[m][j]
    return new_sol