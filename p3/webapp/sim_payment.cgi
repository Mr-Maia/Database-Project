#!/usr/bin/python3
import cgi
import psycopg2

form = cgi.FieldStorage()

order_no = form.getvalue('p_order_no')
cust_no = form.getvalue('p_cust_no')

db_name = "ist1102477"
ist_id = "ist1102477"
password = "lvbq7532"
host = "db.tecnico.ulisboa.pt"
port = "5432"
dsn = ('host={} port={} user={} password={} dbname={}'.format(host, port, ist_id, password, db_name))

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>DBgrupo34</title>')
print('</head>')
print('<body>')

connection = None

try:
    if not (order_no.isdigit() and cust_no.isdigit()):
        raise ValueError('order number and customer number should be numeric values.')
    # Creating connection
    connection = psycopg2.connect(dsn)
    print('<p>Connected<p>')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM orders WHERE order_no = %s', (order_no,))
    order = cursor.fetchone()

    if order is None:
        print("<h1>ERROR: There is no Order with that customer number</h1>")

    cursor.execute('SELECT * FROM customer WHERE cust_no = %s', (cust_no,))
    customer = cursor.fetchone()

    if customer is None:
        print("<h1> ERROR: There is no Client with that customer number</h1>")

    cursor.execute('INSERT INTO pay VALUES (%s, %s)', (order_no, cust_no))
    print("<h1> Payment simulated with success</h1>")
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