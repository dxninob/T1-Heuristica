import sys
sys.path.append('./algorithms')
from xlwt import Workbook
from input_data import read_data
from output_data import write_data
from algorithm1 import constructive
from VND import VND
from Mixed import Mixed
from time import time
import numpy as np


time_limit = {"JSSP1": 2, "JSSP2": 2, "JSSP3": 2, "JSSP4": 2, "JSSP5": 75, "JSSP6": 75, "JSSP7": 75, "JSSP8": 75, "JSSP9": 75, "JSSP10": 75, "JSSP11": 150, "JSSP12": 150, "JSSP13": 300, "JSSP14": 300, "JSSP15": 1800, "JSSP16": 1800}
wbvnd = Workbook()
wbr = Workbook()
sheetwbr = wbr.add_sheet(f'Results')
wbt = Workbook()
sheetwbt = wbt.add_sheet(f'Time')

for instance in range(1,17):
    print(f"Instance{instance}")
    n,m,timep,order = read_data(instance)

    sol, Z = constructive(n,m,timep,order)
    print("constructive:", Z)

    t1 = time()
    new_sol, new_Z = VND(sol, Z, timep, order, n, m, time_limit[f'JSSP{instance}'])
    print("VND:", new_Z)
    t2 = time()
    t = t2 - t1
    write_data(wbvnd, instance, new_sol, new_Z, t)
    sheetwbr.write(1, instance, int(new_Z))
    sheetwbt.write(1, instance, t)

    # nsol = 3; T0 = 10; Tf = 1; L = 10; p = 0.7; nit = 10; nc = 3; r = 5
    # t1 = time()
    # new_sol, new_Z = Mixed(nsol, T0, Tf, L, p, nit, nc, r, n, m, timep, order, time_limit[f'JSSP{instance}'])
    # t2 = time()
    # t = t2 - t1
    # print("Mixed:", new_Z)
    # write_data(wbvnd, instance, new_sol, new_Z, t)
    # sheetwbr.write(1, instance, int(new_Z))
    # sheetwbt.write(1, instance, t)

wbvnd.save("JSSP_Daniela_Nino.xls")
wbr.save("Results.xls")
wbt.save("Time.xls")