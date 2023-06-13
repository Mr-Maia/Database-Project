#!/usr/bin/env python3
import cgi
import psycopg2

# Connect to the PostgreSQL database
# Commit changes and close the database connection

# Function to register a product in the database
def register_product(connection,cursor,form):
    sku = form.getvalue('p_sku')
    name = form.getvalue('p_name')
    description = form.getvalue('p_description')
    price = form.getvalue('p_price')
    ean = form.getvalue('p_ean')

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
    print(" <form action= 'local.HTML'")
    print("     <input type= 'submit' value='Go Back'>")
    print(" </form>")

# Function to remove a product from the database
def remove_product(connection,cursor,form):
    sku = form.getvalue('p_sku')

    cursor.execute("SELECT * FROM product WHERE  SKU = %s",sku)
    check_product = cursor.fetchone()
    if check_product is None:
        print("<h1>ERROR: There is no product with that sku")
        return

    cursor.execute("DELETE FROM product WHERE SKU = %s", sku)
    connection.commit()

    print("<h1>Product removed with success!</h1>")

# Function to register a supplier in the database
def register_supplier(connection,cursor,form):
    tin = form.getvalue('s_tin')
    name = form.getvalue('s_name')
    address = form.getvalue('s_address')
    sku = form.getvalue('s_sku')
    date = form.getvalue('s_date')

    # Code to handle the case where any of the variables is None
    if tin is None or name is None or address is None or sku is None or date is None:
        pass
    elif not tin.isdigit():
        print("<h1>TIN must be a numeric value</h1>")
        print("<p>Error registering supplier</p>")
        return

    sql = 'INSERT INTO supplier (TIN, name, address, sku, date) VALUES (%s, %s, %s, %s, %s)'
    # Execute the INSERT statement
    cursor.execute(sql, (tin, name, address, sku, date))
    connection.commit()
    print("<h1>Supplier registered with success!</h1>")
    print(" <form action= 'local.HTML'")
    print("     <input type= 'submit' value='Go Back'>")
    print(" </form>")

# Function to remove a supplier from the database
def remove_supplier(connection,cursor,form):
    tin = form.getvalue('s_tin')

    cursor.execute("SELECT * FROM supplier WHERE  SKU = %s",tin)
    check_supplier = cursor.fetchone()
    if check_supplier is None:
        print("<h1>ERROR: There is no supplier with that TIN")
        return

    cursor.execute("DELETE FROM supplier WHERE SKU = %s", tin)
    connection.commit()

    print("<h1>Product removed with success!</h1>")

def change_price(connection,cursor,form):
    sku = form.getvalue('p_sku')
    price = form.getvalue('new_price')

    cursor.execute("SELECT * FROM product WHERE SKU = %s", sku)
    check_product = cursor.fetchone()
    if check_product is None:
        print("<h1>ERROR: There is no product with that sku")
        return

    cursor.execute("UPDATE product SET price = %s WHERE SKU = %s", (price, sku))
    connection.commit()
    print("<h1>Product registered with success!</h1>")
    print(" <form action= 'local.HTML'")
    print("     <input type= 'submit' value='Go Back'>")
    print(" </form>")

def change_description(connection,cursor,form):
    sku = form.getvalue('p_sku')
    description = form.getvalue('new_description')

    cursor.execute("SELECT * FROM product WHERE SKU = %s", sku)
    check_product = cursor.fetchone()
    if check_product is None:
        print("<h1>ERROR: There is no product with that sku")
        return

    cursor.execute("UPDATE product SET description = %s WHERE SKU = %s",(description, sku))
    connection.commit()
    print("<h1>Product registered with success!</h1>")
    print(" <form action= 'local.HTML'")
    print("     <input type= 'submit' value='Go Back'>")
    print(" </form>")


def register_customer(connection,cursor,form):
    cust_no = form.getvalue('c_cust_no')
    if not isinstance(cust_no,int) :
        print("<h1>Customer number invalid</h1>")
    name = form.getvalue('c_name')
    if not isinstance(name,str):
        print("<h1>Customer name invalid</h1>")
    cust_email = form.getvalue('c_email')
    cust_phone = form.getvalue('c_phone')
    cust_address = form.getvalue('c_address')
    cursor.execute("INSERT INTO customer VALUES (%s, %s, %s, %s, %s)", (cust_no,name,cust_email,cust_phone,cust_address))
    connection.commit()
    print("<h1>Customer registered with success!</h1>")
    print(" <form action= 'local.HTML'")
    print("     <input type= 'submit' value='Go Back'>")
    print(" </form>")


db_name = "ist1102477"
ist_id = "ist1102477"
password = "lvbq7532"
host = "db.tecnico.ulisboa.pt"
port = "5432"
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

