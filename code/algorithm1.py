import numpy as np


def algorithm1(jobs, machines, time, order):
    j_info = np.zeros((jobs,4), dtype=int)
    m_info = np.zeros(machines, dtype=int)
    m_avl = np.zeros(machines, dtype=int)
    j_avl = np.zeros((machines,jobs), dtype=int)
    t = 0

    while check(j_info, machines):
        m_avl = np.zeros(machines, dtype=int)
        j_avl = np.zeros((machines,jobs), dtype=int)

        for m in range(machines):
            if m_info[m] <= t:
                m_avl[m] = 1

        for m in range(machines):
            if m_avl[m] == 1:
                for j in range(jobs):
                    if j_info[j][0] < machines:
                        if m+1 == order[j][j_info[j][0]]:
                            if j_info[j][1] <= t:
                                j_avl[m][j] = 1

        for m in range(machines):
            t_max = 0
            j_max = 0
            if m_avl[m] == 1:
                if np.any(j_avl[m]):
                    for j in range(jobs):
                        if j_avl[m][j] == 1:
                            if time[j][j_info[j][0]] > t_max:
                                t_max = time[j][j_info[j][0]]
                                j_max = j
                    # m_info[m] = max(t,m_info[m]+t_max)
                    m_info[m] = t + t_max
                    j_info[j_max][0] += 1
                    j_info[j_max][1] = max(j_info[j_max][3], m_info[m])
                    j_info[j_max][2] = t
                    j_info[j_max][3] = t + t_max

        t_prev = t
        t = 1000000000000 # Cambiar por una cota mayor
        for j in j_info:
            if j[3] != 0:
                if j[3] < t:
                    if j[3] > t_prev:
                        t = j[3]
    Z = max(m_info)
    print("Z=",Z)


def check(j_info,machines):
    for j in j_info:
        if j[0] < machines:
            return True
    return False
    

from input_data import read_data

for instance in range(16,17):
    n,m,time,order = read_data(instance)
    algorithm1(n,m,time,order)