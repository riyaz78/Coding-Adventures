import pyodbc

#Define your connection string

server = ''
database = ''
username = ''
password = ''
driver= '{ODBC Driver 18 for SQL Server}'


#Connect to your database
conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

#Create a cursor from the connection
cursor = conn.cursor()

#execute a query
cursor.execute("SELECT * FROM test1")

#Iterate over the results
for row in cursor:
    print(row)

#Close the connection
conn.close()