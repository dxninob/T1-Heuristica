import numpy as np
from methods import feasible, time_Z

# Revisar si debo hacer copias de un objeto
def IBFI(sol, Z, timep, order, jobs, machines):
    stop = False
    while not stop:
        stop = True
        for m in range(machines):
            for j in range(jobs):
                for i in range(j-1, -1, -1):
                    sol_neighbor = move(sol, m, j, i)
                    if feasible(sol_neighbor, order, jobs, machines):
                        Z_neighbor = time_Z(sol_neighbor, timep, order, jobs, machines)
                        if Z_neighbor < Z:
                            stop = False
                            sol = sol_neighbor
                            Z = Z_neighbor
                            break
                    else:
                        break
                if not stop:
                    break
            if not stop:
                break
        # Es necesario este?
        if not stop:
            break
    return sol, Z


def move(sol, m, j, i):
    new_sol = np.copy(sol)
    for k in range(j-1,i-1,-1):
        new_sol[m][k+1] = new_sol[m][k]
    new_sol[m][i] = sol[m][j]
    return new_sol