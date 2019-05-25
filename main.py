import pyodbc
print("Connecting...")
cnxn = pyodbc.connect(driver = "{FreeTDS}", server = "192.168.2.75", database="SorterDB" , 
user="sa", password="server@1314")
print("Connected")

cursor = cnxn.cursor()

cursor.execute('SELECT * FROM [UsersTBL]')

for row in cursor:
    print('row = %r' % (row,))