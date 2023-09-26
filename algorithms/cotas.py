from input_data import read_data
from xlwt import Workbook

wb = Workbook()
sheet = wb.add_sheet(f'cotas')

count=1
for instance in range(1,17):
    n,m,timep,order = read_data(instance)
    
    arr1 = []
    for fila in range(len(timep)):
        total = 0
        for columna in range(len(timep[0])):
            total += timep[fila][columna]
        arr1.append(total)
    # print(arr1)

    arr2 = []
    for maquina in range(m):
        total = 0
        for fila in range(len(timep)):
            for columna in range(len(timep[0])):
                if order[fila][columna] ==  maquina+1:
                    total += timep[fila][columna]
        arr2.append(total)
    # print(arr2)
    cota = max(max(arr1), max(arr2))
    print(cota)
    sheet.write(1, count, int(cota))
    count += 1

wb.save("cotas.xls")