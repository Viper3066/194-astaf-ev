import sqlite3

conn = sqlite3.connect('../Chinook_Sqlite.sqlite')
cursor = conn.cursor()

cursor.execute('''
SELECT Track.Name
            FROM Track            
''')
a = cursor.fetchall()
for i in a:
    print(i)
