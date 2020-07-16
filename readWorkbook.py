from openpyxl import load_workbook

read_workbook = load_workbook('./JusikGall_1_PAGE_2020년7월14일_List.xlsx')
read_cell = read_workbook.active

for i in range(1, 20):
    print(read_cell.cell(i, 2).value)

