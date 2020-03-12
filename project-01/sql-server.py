import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:192.168.1.61'
database = 'TestDB'
username = 'denis'
password = 'denis'
cnxn = pyodbc.connect('DRIVER={/usr/local/lib/libmsodbcsql.17.dylib};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()

#Sample insert query
cursor.execute("INSERT INTO Inventory VALUES (1, 'banana', 150);")
cnxn.commit()
row = cursor.fetchone()

while row:
    print ('Inserted Product key is ' + str(row[0]) )
    row = cursor.fetchone()