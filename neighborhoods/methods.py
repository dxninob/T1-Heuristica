import numpy as np


def feasible(sol, order, jobs, machines):
    next_machine = np.zeros(jobs, dtype=int)
    next_job = np.zeros(machines, dtype=int)

    stop = False
    while not stop:
        # Cantidad de maquinas que no han terminado de procesar todos los trabajos
        avl_machines = 0
        for m in range(machines):
            if next_job[m] < jobs:
                avl_machines += 1

        count = 0
        for m in range(machines):
            if next_job[m] < jobs:
                # Busco el trabajo que sigue por ser proceado en esa máquina en la solución
                job = sol[m][next_job[m]]
                # Comparo si el trabajo ya fue procesado en las maquinas anteriores de su orden
                j = job - 1
                machine = order[j][next_machine[j]]
                if machine == m+1:
                    next_job[m] += 1
                    next_machine[j] += 1
                else:
                    # Cantidad de maquina que no pueden procesar el trabajo siguente
                    count += 1
        # Si este valor es el mismo significa que todos los trabajos ya fueron procesados
        # O que las máquinas no pueden procesar los trabajos siguientes
        if avl_machines == count:
            stop = True

    for j in range(jobs):
        if next_machine[j] < machines:
            # Si una máquina no procesó todos los trabajos es no factible
            return False
    # Si todas las máquinas procesaron todos los trabajos es factible
    return True


def time_Z(sol, timep, order, jobs, machines):
    next_machine = np.zeros(jobs, dtype=int)
    next_job = np.zeros(machines, dtype=int)
    time_machines = np.zeros(machines, dtype=int)
    time_jobs = np.zeros(jobs, dtype=int)

    stop = False
    while not stop:
        stop = True
        for m in range(machines):
            if next_job[m] < jobs:
                job = sol[m][next_job[m]]
                j = job - 1
                machine = order[j][next_machine[j]]
                if machine == m+1:
                    # print("t =", timep[j][next_machine[j]])
                    # print("time_jobs[j] =", time_jobs[j])
                    # print("time_machines[m] =", time_machines[m])
                    time_job_temp = time_jobs[j]
                    time_jobs[j] = max(time_jobs[j], time_machines[m]) + timep[j][next_machine[j]]
                    time_machines[m] = max(time_machines[m], time_job_temp) + timep[j][next_machine[j]]

                    next_job[m] += 1
                    next_machine[j] += 1
                    
                    # print("job =",j, " --- machine =",m, " ----- time_job =",  time_jobs[j])
        
        for j in range(jobs):
            if next_machine[j] < machines:
                stop = False
                break

    return max(time_machines)