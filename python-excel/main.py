import openpyxl
import read_excel, write_excel

wb = openpyxl.load_workbook("master.xlsx")

activeSheet = wb.active

jenkins_list = []
read_excel.readExcel("master.xlsx", jenkins_list)
# read_excel.readExcel("nj3_raw_tagging_invalid_vms.xlsx", jenkins_list)

randeep_list = []
read_excel.readExcel("vsphere.xlsx", randeep_list)

vm_same = []
vm_diff = []

for randeep_item in randeep_list:
    if randeep_item in jenkins_list:
        vm_same.append(randeep_item)
    else:
        vm_diff.append(randeep_item)

for jenkins_item in jenkins_list:
    if jenkins_item not in randeep_list:
        vm_diff.append(jenkins_item)

write_excel.write_excel(vm_same, "vm_same.xlsx")
write_excel.write_excel(vm_diff, "vm_diff.xlsx")

