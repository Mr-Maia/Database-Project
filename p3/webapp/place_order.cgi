#!/usr/bin/python3
import cgi
import psycopg2

form = cgi.FieldStorage()

order_no = form.getvalue('o_order_no')
cust_no = form.getvalue('o_cust_no')
sku = form.getvalue('o_sku')
qty = form.getvalue('o_qty')
date = form.getvalue('o_date')

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

    cursor.execute('SELECT * FROM orders WHERE order_no = %s', (order_no,))
    order = cursor.fetchone()

    if order is not None:
        print("<h1>ERROR: There is already an Order placed with that order number</h1>")

    cursor.execute('SELECT * FROM product WHERE SKU = %s', (sku,))
    product = cursor.fetchone()

    if product is None:
        print("<h1>ERROR: Producto not found</h1>")

    cursor.execute('SELECT * FROM customer WHERE cust_no = %s', (cust_no,))
    customer = cursor.fetchone()

    if customer is None:
        print("<h1>ERROR: There is no Client with that customer number</h1>")

    cursor.execute('INSERT INTO orders VALUES (%s, %s, %s)', (order_no, cust_no, date))
    connection.commit()
    cursor.execute('INSERT INTO contains VALUES (%s, %s, %s)', (order_no, sku, qty))
    print("<h1> Order placed with success</h1>")
    connection.commit()

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
