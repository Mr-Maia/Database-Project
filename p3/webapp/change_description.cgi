#!/usr/bin/python3
import cgi
import psycopg2

form = cgi.FieldStorage()

sku = form.getvalue('p_sku')
description = form.getvalue('new_description')

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

    cursor.execute("SELECT * FROM product WHERE SKU = %s", sku)
    check_product = cursor.fetchone()
    if check_product is None:
        print("<h1>ERROR: There is no product with that sku")
        pass

    cursor.execute('UPDATE product SET description = %s WHERE SKU = %s', (description, sku))
    connection.commit()
    print("<h1>Description changed with success!</h1>")

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