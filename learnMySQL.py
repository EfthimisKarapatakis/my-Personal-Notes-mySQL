import mysql.connector

# This is always on top:
mydb = mysql.connector.connect(
    host="localhost",
    user="YOUR_USER_NAME",
    password="YOUR_PERSONAL_PASSWARD",
    database = "mydatabase"
)


myCursor = mydb.cursor()

# Create a database:
"""
myCursor.execute("CREATE DATABASE mysdatabase")
"""

# Check if database exists:
"""
myCursor.execute("SHOW DATABASES")
for x in myCursor: # type: ignore
    print(x)
"""

# Create a table:
"""
myCursor.execute("CREATE TABLE (name VARCHAR(255), address VARCHAR(255))")
"""

# Check if table exists:
"""
myCursor.execute("SHOW TABLES")
for x in myCursor: # type: ignore
    print(x)
"""

# Delete a table
"""
myCursor.execute("DROP TABLE table_name")
"""

# Primary key (When creating a table, you should also create a column with a unique key for each record):
"""
# When the table doesnt exists:
'''Primary key: INT AUTO_INCREMENT PRIMARY KEY
myCursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
'''#                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# If the table already exists:
'''
myCursor.execute("ALTER TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
'''
"""

# Insert in a table:
"""
''' One row:
sql = "INSERT INTO  customers (name, address) VALUE (%s, %s)"
val = ("John", "london")
myCursor.execute(sql, val)

mydb.commit() # It is required to make the changes, otherwise no changes are made to the table.

print(myCursor.rowcount, "record inserted.")
'''

''' Multiple rows:
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]
myCursor.executemany(sql, val)

mydb.commit()

print(myCursor.rowcount, "record inserted")
'''
"""

# Get inserted id:
"""
sql = "INSERT INTO customers (name, address) VALUE (%s, %s)"
val = ("Michelle", "Blue Village")
myCursor.execute(sql, val)

mydb.commit()
print(myCursor.rowcount, "record inserted, ID = ", myCursor.lastrowid)
"""

# Select from a table:
"""
myCursor.execute("SELECT * FROM customers")

myresult = myCursor.fetchall()

for x in myresult:
    print(x)
"""

# Selecting columns:
"""
myCursor.execute("SELECT name, address FROM customers")

myResult = myCursor.fetchall()

for x in myResult:
    print(x)
"""

# Select only one row:
"""
myCursor.execute("SELECT * FROM customers")

myresult = myCursor.fetchone()

print(myresult)
"""

# Select with a filter:
"""
sql = "SELECT * FROM customers WHERE name = 'john'"
myCursor.execute(sql)

myResult = myCursor.fetchall()

for x in myResult:
    print(x)
"""

# Wildcard Characters
"""
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

myCursor.execute(sql)

myresult = myCursor.fetchall()

for x in myresult:
    print(x)
"""

# Prevent sql injections:

"""
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

myCursor.execute(sql, adr)

myresult = myCursor.fetchall()

for x in myresult:
    print(x)
"""

# Sort the Result:
"""
sql = "SELECT * FROM customers ORDER BY name" # DESC" : reverse alphabetically

myCursor.execute(sql)

myResolt = myCursor.fetchall()

for x in myResolt:
    print(x)
"""

# Delete record:
"""
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
myCursor.execute(sql)

''' To prevent the sql injections:
sql = "DELETE FROM customers WHERE address = %s"
adr = ('Yellow Garden 2', )
myCurson.execute(sql, adr)

'''


mydb.commit()

print(myCursor.rowcount, "record(s) deleted")
"""

# Delete table if it exists:
"""
sql = "DROP TABLE IF EXISTS customers"
myCursor.execute(sql)
"""

# Update table:
"""
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)

mydb.commit()
print(myCursor.rowcount, "record(s) affected")
"""

# Limit the result:
"""
sql = "SELECT * FROM customers LIMIT 5"
myCursor.execute(sql)

myResult = myCursor.fetchall()

for x in myResult:
    print(x)
"""

# Start From Another Position
"""
sql = "SELECT * FROM customers LIMIT 5 OFFSET 2"
myCursor.execute(sql)

myResult = myCursor.fetchall()

for x in myResult:
    print(x)
"""
