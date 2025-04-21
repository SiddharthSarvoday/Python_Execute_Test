import pandas as pd
import pydoc as odbc
import glob
import os
import xlsxwriter
from xlsxwriter.worksheet import Worksheet

def main():

    workbook = xlsxwriter.Workbook('Python_Output_Results.xlsx')
    Worksheet = workbook.add_worksheet('Data')
    Worksheet.write('A1','No. of days')
    Worksheet.write('B1','Days')
    Worksheet.write('C1','Time Stamp')

    Worksheet.write('A2','Day 1')
    Worksheet.write('A3','Day 2')
    Worksheet.write('A4','Day 3')
    Worksheet.write('A5','Day 4')

    Worksheet.write('B2','Check 1')
    Worksheet.write('B3','Check 2')
    Worksheet.write('B4','Check 3')
    Worksheet.write('B5','Check 4')

    Worksheet.write('C2','XXX')
    Worksheet.write('C3','XXX')
    Worksheet.write('C4','XXX')
    Worksheet.write('C4','XXX')

    workbook.close()

if __name__ == '__main__':
    main()



