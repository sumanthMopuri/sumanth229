from xlwt import Workbook
wb=Workbook()
sheet1=wb.add_sheet("Sheet1")
sheet2=wb.add_sheet("Sheet2")
sheet1.write(1,0,'a')
sheet2.write(0,1,'b')
wb.save('example1.xlxs')



"""import xlrd
wb=xlrd.open_workbook("example1.xlxs")
sheet=wb.sheet_by_index(0)
for i in range(sheet.nrows):
    print(sheet.row.values(i))
    
for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        print(sheet.cell_value(i,j),end=" ")
        print()"""
