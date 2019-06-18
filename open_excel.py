from __future__ import print_function
import unittest
import os.path
import win32com.client

class ExcelMacro(unittest.TestCase):
    def test_excel_macro(self):
        try:
            xlApp = win32com.client.DispatchEx('Excel.Application')
            xlsPath = os.path.expanduser('F:\\Palimontes\\Planilha Teste.xlsm')
            wb = xlApp.Workbooks.Open(Filename=xlsPath)
            xlApp.Run('Macro1')
            wb.Save()
            xlApp.Quit()
            print("Macro ran successfully!")
        except:
            print("Error found while running the excel macro!")
            xlApp.Quit()
if __name__ == "__main__":
    unittest.main()
