#!/usr/bin/python3
import cgi
import psycopg2
import configparser

form = cgi.FieldStorage()

order_no = form.getvalue('o_order_no')
cust_no = form.getvalue('o_cust_no')
sku = form.getvalue('o_sku')
qty = form.getvalue('o_qty')
date = form.getvalue('o_date')

config = configparser.ConfigParser()
config.read('config.ini')

db_name = config.get('database', 'db_name')
ist_id = config.get('database', 'ist_id')
password = config.get('database', 'password')
host = config.get('database', 'host')
port = config.get('database', 'port')
dsn = 'host={} port={} user={} password={} dbname={}'.format(host, port, ist_id, password, db_name)

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>DBgrupo34</title>')
print('<style>')
print('input[type="submit"] {')
print('    display: block;')
print('    width: 50%;')
print('    padding: 10px;')
print('    margin-top: 20px;')
print('    background-color: #FF325D;')
print('    color: white;')
print('    border: none;')
print('    border-radius: 4px;')
print('    cursor: pointer;')
print('}')
print('</style>')
print('</head>')
print('<body>')

connection = None

try:
    if not (order_no.isdigit() and cust_no.isdigit() and sku.isdigit() and qty.isdigit()):
        raise ValueError('order number/customer number/sku/quantity should be numeric values.')
    # Creating connection
    connection = psycopg2.connect(dsn)
    print('<p>Connected<p>')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM supplier WHERE sku = %s', (sku,))
    supplier = cursor.fetchone()
    if supplier is None:
        print('<h1><h1> No supplier found for this product</h1>')
        print("<form action='local.html'>")
        print("<input type='submit' value='Return to main menu'>")
        print('</form>')
        print('</body>')
        print('</html>')
        raise ValueError()

    cursor.execute('SELECT * FROM orders WHERE order_no = %s', (order_no,))
    order = cursor.fetchone()

    if order is not None:
        print('<h1><h1> There is already an Order placed with that order number</h1>')
        print("<form action='local.html'>")
        print("<input type='submit' value='Return to main menu'>")
        print('</form>')
        print('</body>')
        print('</html>')
        raise ValueError()

    cursor.execute('SELECT * FROM product WHERE SKU = %s', (sku,))
    product = cursor.fetchone()

    if product is None:
        print('<h1><h1> Product not found</h1>')
        print("<form action='local.html'>")
        print("<input type='submit' value='Return to main menu'>")
        print('</form>')
        print('</body>')
        print('</html>')
        raise ValueError()

    cursor.execute('SELECT * FROM customer WHERE cust_no = %s', (cust_no,))
    customer = cursor.fetchone()

    if customer is None:
        print("<h1>ERROR: There is no Client with that customer number</h1>")
        print("<form action='local.html'>")
        print("<input type='submit' value='Return to main menu'>")
        print('</form>')
        print('</body>')
        print('</html>')
        raise ValueError()

    cursor.execute('INSERT INTO orders VALUES (%s, %s, %s)', (order_no, cust_no, date))
    connection.commit()
    cursor.execute('INSERT INTO contains VALUES (%s, %s, %s)', (order_no, sku, qty))
    print("<h1> Order placed with success</h1>")
    print("<form action='local.html'>")
    print("<input type='submit' value='Return to main menu'>")
    print('</form>')
    print('</body>')
    print('</html>')
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