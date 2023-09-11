from xlwt import Workbook
from input_data import read_data
from output_data import write_data
from algorithm1 import algorithm1
from algorithm2 import algorithm2
from time import time

wb0 = Workbook()
wb1 = Workbook()
# wb2 = Workbook()

for instance in range(1,17):
    n,m,timep,order = read_data(instance)

    t1 = time()
    sol,Z = algorithm1(n,m,timep,order)
    t2 = time()
    t = t2 - t1
    write_data(wb0, instance, sol, Z, t)

    r = 10 # Noise
    t1 = time()
    sol,Z = algorithm2(n,m,timep,order,r)
    t2 = time()
    t = t2 - t1
    write_data(wb1, instance, sol, Z, t)

wb0.save("JSSP_Daniela_Nino_constructivo.xls")
wb1.save("JSSP_Daniela_Nino_ruido.xls")
# wb2.save("JSSP_Daniela_Nino_3.xls")