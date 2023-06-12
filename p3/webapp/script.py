#!/usr/bin/env python3
import cgi
import cgitb
import psycopg2

# Connect to the PostgreSQL database
# Commit changes and close the database connection

# Function to register a product in the database
def register_product(connection,cursor,form):
    sku = form.getvalue('sku')
    name = form.getvalue('name')
    description = form.getvalue('description')
    price = form.getvalue('price')
    ean = form.getvalue('ean')

    # Code to handle the case where any of the variables is None
    if sku is None or name is None or description is None or price is None or ean is None:
        pass
    elif not ean.isdigit():
        print("<h1>EAN must be a numeric value</h1>")
        print("<p>Error registering product</p>")
        return

    sql = 'INSERT INTO product (SKU, name, description, price, ean) VALUES (%s, %s, %s, %s, %s)'
    # Execute the INSERT statement
    cursor.execute(sql, (sku, name, description, price, ean))
    connection.commit()
    print("<h1>Product registered with success!</h1>")

# Function to remove a product from the database
def remove_product(connection,cursor,form):
    sku = form.getvalue('sku')

    cursor.execute("SELECT * FROM product WHERE  SKU = %s",sku)
    check_product = cursor.fetchone()
    if check_product is None:
        print("<h1>ERROR: There is no product with that sku")
        return

    cursor.execute("DELETE FROM product WHERE SKU = %s", sku)
    connection.commit()

    print("<h1>Product removed with success!</h1>")

# Function to register a supplier in the database
def register_supplier(tin, name, address, sku, date, conn, cursor):
    try:
        # Execute the INSERT statement
        cursor.execute("INSERT INTO supplier (TIN, name, address, SKU, date) VALUES (%s, %s, %s, %s, %s)",
                       (tin, name, address, sku, date))
        print("Content-Type: text/html")
        print()
        print("Supplier registered successfully!")
    except psycopg2.Error as e:
        print("Content-Type: text/html")
        print()
        print("Error registering supplier:", e)

# Function to remove a supplier from the database
def remove_supplier(tin, conn, cursor):
    try:
        # Execute the DELETE statement
        cursor.execute("DELETE FROM supplier WHERE TIN = %s", (tin,))
        print("Content-Type: text/html")
        print()
        print("Supplier removed successfully!")
    except psycopg2.Error as e:
        print("Content-Type: text/html")
        print()
        print("Error removing supplier:", e)


db_name = "ist1102477"
ist_id = "ist1102477"
password = "lvbq7532"
host = "db.tecnico.ulisboa.pt"
port = "5432"
connection = None
dsn = ('host={} port={} user={} password={} dbname={}'.format(host, port, ist_id, password, db_name))

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Lab 09</title>')
print('</head>')
print('<body>')

connection = None

try:

    # Creating connection
    connection = psycopg2.connect(dsn)
    print('<p>Connected<p>')
    cursor = connection.cursor()

    form = cgi.FieldStorage()

    if any(value == "register_product" for value in form.keys()):
        register_product(connection, cursor, form)
    elif any(value == "remove_product" for value in form.keys()):
        remove_product(connection,cursor,form)
    elif any(value == "register_supplier" for value in form.keys()):
        register_product(connection, cursor, form)
    elif any(value == "remove_supplier" for value in form.keys()):
        remove_product(connection,cursor,form)
    else:
        print('<p>ERROR')

    cursor.close()

except Exception as exp:
    # Print errors on the webpage if they occur
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(exp))
finally:
    if connection is not None:
        connection.close()
    print('</body>')
    print('</html>')

