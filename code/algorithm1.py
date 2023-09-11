import numpy as np


def algorithm1(jobs, machines, timep, order):
    j_info = np.zeros((jobs,4), dtype=int)
    m_info = np.zeros(machines, dtype=int)
    m_avl = np.zeros(machines, dtype=int)
    m_pos = np.zeros(machines, dtype=int)
    j_avl = np.zeros((machines,jobs), dtype=int)
    sol = np.zeros((machines,jobs), dtype=int)
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
            t_max = 10000000 # Cambiar a un numero max
            j_max = 0
            if m_avl[m] == 1:
                if np.any(j_avl[m]):
                    for j in range(jobs):
                        if j_avl[m][j] == 1:
                            if timep[j][j_info[j][0]] < t_max:
                                t_max = timep[j][j_info[j][0]]
                                j_max = j
                    sol[m][m_pos[m]] = j_max+1
                    m_info[m] = t + t_max
                    m_pos[m] += 1
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
    return (sol,Z)


def check(j_info,machines):
    for j in j_info:
        if j[0] < machines:
            return True
    return False
