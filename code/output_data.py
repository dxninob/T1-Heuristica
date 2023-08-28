def write_data(wb, num, sol, Z, t):
    sheet = wb.add_sheet(f'JSSP{num}')
    row = 0
    while row < len(sol):
        for col in range(len(sol[0])):
            sheet.write(row, col, sol[row][col])
        row += 1
    sheet.write(row, 0, Z)
    sheet.write(row, 1, t)