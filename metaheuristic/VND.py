import numpy as np
import sys
sys.path.append('./intensification')
# from Insertion_Backward_Best_Improvement import IBBI
from Insertion_Backward_First_Improvement import IBFI
# from Insertion_Forward_Best_Improvement import IFBI
from Insertion_Forward_First_Improvement import IFFI
# from Interchange_Best_Improvement import IBI
from Interchange_First_Improvement import IFI
from time import time


def VND(sol, Z, timep, order, jobs, machines, time_limit):
    t1 = time()
    current_time = 0
    num_neighborhoods = 3
    neighborhood = 1
    
    while current_time < time_limit and neighborhood <= num_neighborhoods:
        if neighborhood == 1:
            # Insertion Forward
            sol_neighbor, Z_neighbor = IFFI(sol, Z, timep, order, jobs, machines)
        elif neighborhood == 2:
            # Insertion Backward
            sol_neighbor, Z_neighbor = IBFI(sol, Z, timep, order, jobs, machines)
        elif neighborhood == 3:
            # Interchange Forward
            sol_neighbor, Z_neighbor = IFI(sol, Z, timep, order, jobs, machines)
        
        if Z_neighbor < Z:
            neighborhood = 1
            sol = sol_neighbor
            Z = Z_neighbor
        else:
            neighborhood += 1
        
        t2 = time()
        current_time = t2 - t1

    return sol, Z