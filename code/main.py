from xlwt import Workbook
from input_data import read_data
from output_data import write_data
from algorithm1 import algorithm1


wb0 = Workbook()
# wb1 = Workbook()
# wb2 = Workbook()

for instance in range(1,4):
    
    n,m,time,order = read_data(instance)
    sol,Z,f = algorithm1(n,m,time,order)
    write_data(wb0, instance, sol, Z, f)

wb0.save("JSSP_Daniela_Nino_1.xls")
# wb1.save("JSSP_Daniela_Nino_2.xls")
# wb2.save("JSSP_Daniela_Nino_3.xls")