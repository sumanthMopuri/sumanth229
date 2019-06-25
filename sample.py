Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import xlrd
>>> wb=xlrd.open_workbook("example1.xls")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    wb=xlrd.open_workbook("example1.xls")
  File "C:\Users\princess\AppData\Roaming\Python\Python37\site-packages\xlrd\__init__.py", line 111, in open_workbook
    with open(filename, "rb") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'example1.xls'
>>> wb=xlrd.Workbook()
