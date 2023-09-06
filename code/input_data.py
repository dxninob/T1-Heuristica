import numpy as np


def read_data(num):
    path = f"./JSSP Instances/JSSP{num}.txt"
    with open(path) as f:
        n,m = f.readline().split()
        n = int(n)
        m = int(m)

        time = np.zeros((n,m), dtype=np.int)
        for i in range(n):
            line = f.readline().split()
            line = [int(x) for x in line]
            time[i] = line

        order = np.zeros((n,m), dtype=np.int)
        for i in range(n):
            line = f.readline().split()
            line = [int(x) for x in line]
            order[i] = line
    return((n,m,time,order))