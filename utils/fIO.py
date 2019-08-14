## 文件(excel,csv,text)IO相关
import os
import xlwt
import xlrd
import csv
import pandas as pd
from pandas import DataFrame

pathdefault = '/data/stock_new/'

'''
File
'''
def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
    
'''
Pandas Dataframe
'''
def pdToExcel(fileName, df, path = pathdefault, sheet_name = 'sheet1'):
    with pd.ExcelWriter(path + fileName + '.xlsx') as writer:
        df.to_excel(writer, sheet_name = sheet_name)
        
def pdFromExcel(fileName, path = pathdefault, sheet_name = 'sheet1'):
    df = pd.read_excel(path + fileName + '.xlsx', sheet_name = sheet_name)
    return df

def pdToCsv(fileName, df, path = pathdefault):
    df.to_csv(pathdefault + fileName + '.csv', index = False)

def pdFromCsv(fileName, path = pathdefault, names = []):
    df = pd.read_csv(pathdefault + fileName + '.csv', header = None, names = None)
    return df

  
'''
Text
'''
def fromText(fileName, path = pathdefault):
    with open(path + fileName + '.txt', 'r') as f:
        content = f.read()
    return content
    
def fromTextByLines(fileName, path = pathdefault):
    with open(path + fileName + '.txt', 'r') as f:
        content = f.readlines()
    return content

def toText(fileName, content, path = pathdefault):
    mkdir(path)
    with open(path + fileName + '.txt', 'w') as f:
        f.write(content)

'''
Excel
'''
def toExcel(fileName, content, path = pathdefault, SheetName = 'Sheet1'):
    mkdir(path)
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(SheetName, cell_overwrite_ok=True)
    for row in range(len(content)):
        for col in range(len(content[row])):
            sheet.write(row, col, content[row][col])
    workbook.save(path + fileName + '.xls')

def fromExcel(fileName, path = pathdefault): 
    try:
        workbook = xlrd.open_workbook(path + fileName + '.xls')
    except FileNotFoundError as e:
        workbook = xlrd.open_workbook(path + fileName + '.xlsx')
    sheet = workbook.sheets()[0]
    content = []
    for row in range(sheet.nrows):
        rowData = sheet.row_values(row)
        content.append(rowData)
    return content
    
        
'''
Csv
'''
def fromCsv(fileName, path = pathdefault):   
    with open(path + fileName + '.csv') as f:
        f_csv = csv.reader(f)
        content = []
        for row in f_csv:
            content.append(row)
        return content

def toCsv(fileName, content, path = pathdefault):
    pd_content = DataFrame(content[1:], columns = content[0])
    pd_content.to_csv(pathdefault + fileName + '.csv', index = False)