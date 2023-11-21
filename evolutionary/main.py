import numpy as np
from xlwt import Workbook
from time import time
import sys
sys.path.append('./algorithms')
from input_data import read_data
from output_data import write_data
from GA import GA


time_limit = {'JSSP1': 2, 'JSSP2': 2, 'JSSP3': 2, 'JSSP4': 2, 'JSSP5': 75, 'JSSP6': 75, 'JSSP7': 75, 'JSSP8': 75, 'JSSP9': 75, 'JSSP10': 75, 'JSSP11': 150, 'JSSP12': 150, 'JSSP13': 300, 'JSSP14': 300, 'JSSP15': 1800, 'JSSP16': 1800}
wb = Workbook()
for instance in range(1, 8):

    print(f'Instance{instance}')
    n,m,timep,order = read_data(instance)

    nsol = 10; nc = 5; prob_muta = 0.2; prob_LS = 0.8; r_noise = 5
    t1 = time()
    new_sol, new_Z = GA(nsol, nc, prob_muta, prob_LS, r_noise, n, m, timep, order, time_limit[f'JSSP{instance}'])
    t2 = time()
    t = t2 - t1
    print(new_Z)

    write_data(wb, instance, new_sol, new_Z, t)

wb.save(f'JSSP_Daniela_Nino_GA.xls')