import sqlite3

conn = sqlite3.connect('../Chinook_Sqlite.sqlite')
cursor = conn.cursor()
cursor.execute('''
SELECT Album.Title,COUNT(Track.UnitPrice)
FROM Album 
JOIN Track ON Track.TrackId=InvoiceLine.TrackId 
JOIN InvoiceLine ON Album.AlbumId=Track.AlbumId
  GROUP BY Album.AlbumId;    
''')
a=cursor.fetchall()
for i in a:
    print(i)
