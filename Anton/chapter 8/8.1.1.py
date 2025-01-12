import sqlite3

conn = sqlite3.connect('../Chinook_Sqlite.sqlite')
cursor = conn.cursor()

cursor.execute('''
SELECT Customer.CustomerId, Customer.FirstName, Customer.LastName, COUNT(Invoice.InvoiceId)
FROM Customer 
JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Customer.CustomerId;
               ''')
a = cursor.fetchall()
for i in a:
    print(i)
