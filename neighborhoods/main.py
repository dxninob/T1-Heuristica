import sys
sys.path.append('./algorithms')
from input_data import read_data
from algorithm1 import constructive
from time import time
from methods import feasible
from methods import time_Z

for instance in range(0,17):
    n,m,timep,order = read_data(instance)
    t1 = time()
    sol,Z = constructive(n,m,timep,order)
    t2 = time()
    t = t2 - t1
    print(time_Z(sol, timep, order, n, m))
    print(time_Z(sol, timep, order, n, m))