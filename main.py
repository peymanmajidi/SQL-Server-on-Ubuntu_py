#import libraries
import pyodbc

print("Connecting...")

cnxn = pyodbc.connect(driver = "{FreeTDS}", server = "192.168.2.75", database="MyDB", user="peyman", password="1234567890")

print("Connected")

# make a cursor
cursor = cnxn.cursor()


# write the mssql query
cursor.execute('SELECT * FROM [UsersTBL]')

for row in cursor:
    print('row = %r' % (row,))
    print(f'Username: {row.username}')