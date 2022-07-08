import win32com.client as win32
import pathlib

filePath = pathlib.Path(r"C:\\Users\\cmc.nhduy1\\Desktop\\python-lab", "add_a_workbook.xlsx")
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Add()
wb.SaveAs(str(filePath))
excel.Application.Quit()