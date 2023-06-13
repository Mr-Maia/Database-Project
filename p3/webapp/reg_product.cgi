#!/usr/bin/python3
import cgi
import psycopg2

form = cgi.FieldStorage()

sku = form.getvalue('p_sku')
name = form.getvalue('p_name')
description = form.getvalue('p_description')
price = form.getvalue('p_price')
ean = form.getvalue('p_ean')

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

    sql = 'INSERT INTO product (SKU, name, description, price, ean) VALUES (%s, %s, %s, %s, %s)'
    # Execute the INSERT statement
    cursor.execute(sql, (sku, name, description, price, ean))
    print("<h1> Product registered with success</h1>")
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