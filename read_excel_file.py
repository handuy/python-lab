import win32com.client as win32
import pathlib

class App:
    pass
    
filePath = pathlib.Path(r"C:\\Users\\cmc.nhduy1\\Desktop\\SecureWifi", "account.xlsx")
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Open(str(filePath))
excel.Visible = True

attr_list = []


listApp = []

for sheet in wb.Sheets:

    # sheet.Cells(row, column)
    lastCol = sheet.UsedRange.Columns.Count
    lastRow = sheet.UsedRange.Rows.Count

    currentRow = 1
    currentCol = 1
    while currentCol <= lastCol:
        cellValue = sheet.Cells(currentRow,currentCol).Value
        attr_list.append(cellValue)
        currentCol += 1

    print("attr_list", attr_list)

    currentRow = 2
    while currentRow <= lastRow:
        newApp = App()
        currentCol = 1

        while currentCol <= lastCol:
            cellValue = sheet.Cells(currentRow,currentCol).Value
            setattr(newApp, attr_list[currentCol-1], cellValue)
            currentCol += 1

        listApp.append(newApp)

        currentRow += 1

    attr_list = []

for app in listApp:
  print(app.__dict__)