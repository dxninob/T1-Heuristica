import numpy as np
import random


def grasp(jobs, machines, timep, order,k):
    j_info = np.zeros((jobs,4), dtype=int)
    m_info = np.zeros(machines, dtype=int)
    m_avl = np.zeros(machines, dtype=int)
    m_pos = np.zeros(machines, dtype=int)
    sol = np.zeros((machines,jobs), dtype=int)
    t = 0
    cota = np.sum(timep)

    while check(j_info, machines):
        for m in range(machines):
            if m_info[m] <= t:
                m_avl[m] = 1
            else:
                m_avl[m] = 0

        j_avl_count = np.zeros(machines,dtype=int)
        j_avl = np.zeros((machines,jobs), dtype=int)
        for m in range(machines):
            if m_avl[m] == 1:
                for j in range(jobs):
                    if j_info[j][0] < machines:
                        if m+1 == order[j][j_info[j][0]]:
                            if j_info[j][1] <= t:
                                j_avl[m][j] = 1
                                j_avl_count[m] += 1

        for m in range(machines):
            if m_avl[m] == 1:
                if np.any(j_avl[m]):
                    t_max,j_max = select_job(m,jobs,j_avl,j_info,timep,cota,k,j_avl_count[m])
                    sol[m][m_pos[m]] = j_max+1
                    m_info[m] = t + t_max
                    m_pos[m] += 1
                    j_info[j_max][0] += 1
                    j_info[j_max][1] = max(j_info[j_max][3], m_info[m])
                    j_info[j_max][2] = t
                    j_info[j_max][3] = t + t_max

        t_prev = t
        t = cota
        for m in range(len(m_info)):
            if m_info[m] < t:
                if m_info[m] > t_prev:
                    t = m_info[m]

    Z = max(m_info)
    return (sol,Z)


def check(j_info,machines):
    for j in j_info:
        if j[0] < machines:
            return True
    return False


def select_job(m,jobs,j_avl,j_info,timep,cota,k,count):
    sorted_pos = np.zeros(count, dtype=int)
    sorted_time = np.zeros(count, dtype=int)
    i = 0
    for j in range(jobs):
        if j_avl[m][j] == 1:
            sorted_time[i] = timep[j][j_info[j][0]]
            sorted_pos[i] = j
            i += 1
    sorted_time, sorted_pos = bubbleSort(sorted_time, sorted_pos)
    k = min(k, count)
    rand = random.randrange(0, k)
    t_max = sorted_time[rand] 
    j_max = sorted_pos[rand]  
    return (t_max,j_max)


def bubbleSort(arr, arr2):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
    return (arr, arr2)