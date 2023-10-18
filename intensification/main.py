import sys
sys.path.append('./algorithms')
from xlwt import Workbook
from input_data import read_data
from output_data import write_data
from algorithm1 import constructive
from time import time
from Insertion_Backward_Best_Improvement import IBBI
from Insertion_Backward_First_Improvement import IBFI
from Insertion_Backward_Best_Improvement import IFBI
from Insertion_Backward_First_Improvement import IFFI
from Interchange_Best_Improvement import IBI
from Interchange_First_Improvement import IFI

wb = [Workbook() for _ in range(7)]
wbr = Workbook()
sheetwbr = wbr.add_sheet(f'wbr')
wbt = Workbook()
sheetwbt = wbt.add_sheet(f'wbt')

for instance in range(1,6):
    print(f"Instance{instance}")
    n,m,timep,order = read_data(instance)

    t1 = time()
    sol,Z = constructive(n,m,timep,order)
    print("constructive:", Z)
    t2 = time()
    t = t2 - t1
    write_data(wb[0], instance, sol, Z, t)
    sheetwbr.write(0, instance, int(Z))
    sheetwbt.write(0, instance, t)

    t1 = time()
    new_sol, new_Z = IBBI(sol, Z, timep, order, n, m)
    print("IBBI:", new_Z)
    t2 = time()
    t = t2 - t1
    write_data(wb[1], instance, new_sol, new_Z, t)
    sheetwbr.write(1, instance, int(new_Z))
    sheetwbt.write(1, instance, t)

    t1 = time()
    new_sol, new_Z = IBFI(sol, Z, timep, order, n, m)
    print("IBFI:", new_Z)
    t2 = time()
    t = t2 - t1
    write_data(wb[2], instance, new_sol, new_Z, t)
    sheetwbr.write(2, instance, int(new_Z))
    sheetwbt.write(2, instance, t)

    t1 = time()
    new_sol, new_Z = IFBI(sol, Z, timep, order, n, m)
    print("IFBI:", new_Z)
    t2 = time()
    t = t2 - t1
    write_data(wb[3], instance, new_sol, new_Z, t)
    sheetwbr.write(3, instance, int(new_Z))
    sheetwbt.write(3, instance, t)

    t1 = time()
    new_sol, new_Z = IFFI(sol, Z, timep, order, n, m)
    print("IFFI:", new_Z)
    t2 = time()
    t = t2 - t1
    write_data(wb[4], instance, new_sol, new_Z, t)
    sheetwbr.write(4, instance, int(new_Z))
    sheetwbt.write(4, instance, t)

    t1 = time()
    new_sol, new_Z = IBI(sol, Z, timep, order, n, m)
    print("IBI:", new_Z)
    t2 = time()
    t = t2 - t1
    write_data(wb[5], instance, new_sol, new_Z, t)
    sheetwbr.write(5, instance, int(new_Z))
    sheetwbt.write(5, instance, t)

    t1 = time()
    new_sol, new_Z = IFI(sol, Z, timep, order, n, m)
    print("IFI:", new_Z)
    t2 = time()
    t = t2 - t1
    write_data(wb[6], instance, new_sol, new_Z, t)
    sheetwbr.write(6, instance, int(new_Z))
    sheetwbt.write(6, instance, t)

wb[0].save("JSSP_Daniela_Nino_constructive.xls")
wb[1].save("JSSP_Daniela_Nino_IBBI.xls")
wb[2].save("JSSP_Daniela_Nino_IBFI.xls")
wb[3].save("JSSP_Daniela_Nino_IFBI.xls")
wb[4].save("JSSP_Daniela_Nino_IFFI.xls")
wb[5].save("JSSP_Daniela_Nino_IBI.xls")
wb[6].save("JSSP_Daniela_Nino_IFI.xls")
wbr.save("Results.xls")
wbt.save("Time.xls")