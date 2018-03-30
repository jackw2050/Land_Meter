
import sqlite3
# https://docs.python.org/2/library/sqlite3.html

conn = sqlite3.connect('example.db')

c = conn.cursor()
#
# # Create table
# c.execute('''CREATE TABLE stocks
#              (date text, trans text, symbol text, qty real, price real)''')
#
# # Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#
# # Save (commit) the changes
# conn.commit()

for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print (row)


# need fine and replace method


# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()