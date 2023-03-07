import pyodbc


connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=byltinsyte-dev-sql-server-eu.database.windows.net;'
                          'DATABASE=Monitor;'
                          'UID=byltinsytesqladmin;'
                          'PWD=bf534015-fa65-4d38-a438-42548e4536cc;')
conn = connection
cursor = conn.cursor()