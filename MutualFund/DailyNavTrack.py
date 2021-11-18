from mftool import Mftool
import pandas as pd
import xlsxwriter


#code to convert excel column values into list


df = pd.read_excel("../mutualfund.xlsx") # can also index sheet by name or fetch all sheets
code_list = df['code'].tolist()
print(code_list)


#Code to convert each element of list into list
def extractDigits(lst):
    res = []
    for el in lst:
        sub = str(el).split(', ')
        res.append(sub)

    return (res)

code_list_e= extractDigits(code_list)
print(code_list_e)
#Instantiate mftool.
mf = Mftool()

count=len(code_list_e)
print("Total count "+str(count))
#Iterate nav for current date
for index, code in enumerate(code_list):
    scheme_quotes=mf.get_scheme_quote(code)
    code_list_e[index].append(scheme_quotes['scheme_name'])
    code_list_e[index].append(scheme_quotes['last_updated'])
    code_list_e[index].append(scheme_quotes['nav'])
    count-=1
    print(count)


column_list=["code","mutual fund","date","nav","change"]
code_list_e.insert(0,column_list)

#print(code_list_e)

#write final upgraded list into excel


with xlsxwriter.Workbook("../mutualfund.xlsx") as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(code_list_e):
        worksheet.write_row(row_num, 0, data)

