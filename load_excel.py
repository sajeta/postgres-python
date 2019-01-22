# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 21:40:33 2019

@author: marin
"""

import config as cf
from xlrd import open_workbook

excel_info = cf.excelInfo()
file = excel_info["file_name"]

#loads data from excel file, into a list of lists of tuples
#if empty_rows is set to True than this function will load empty rows
def loadExcel(file=file, empty_rows = False):
    wb = open_workbook(file)
    values = []
    if(empty_rows == True):
        for s in wb.sheets():
            if(s.name == "Popis planirane opreme"):
                #print 'Sheet:',s.name
                for row in range(1, s.nrows):
                    col_names = s.row(0)
                    col_value = []
                    for name, col in zip(col_names, range(s.ncols)):
                        value  = (s.cell(row,col).value)
                        if(name.value != ""):
                            if(type(value) is float):
                                col_value.append((name.value, int(value)))
                            else:
                                col_value.append((name.value, value))
                    values.append(col_value)
    else:
        for s in wb.sheets():
            if(s.name == "Popis planirane opreme"):
                #print 'Sheet:',s.name
                for row in range(1, s.nrows):
                    col_names = s.row(0)
                    col_value = []
                    for name, col in zip(col_names, range(s.ncols)):
                        value  = (s.cell(row,col).value)
                        if(name.value != ""):
                            if(s.cell(row,1).value != "" or s.cell(row,2).value != "" or s.cell(row,3).value != ""):
                                if(type(value) is float):
                                    col_value.append((name.value, int(value)))
                                else:
                                    col_value.append((name.value, value))
                    if(len(col_value) > 0 ):
                        values.append(col_value)
    
    columns = []
    for c in values[0]:
        columns.append(c[0])
        
    return values, columns