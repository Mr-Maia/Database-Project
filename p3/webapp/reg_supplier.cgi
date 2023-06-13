#!/usr/bin/python3
import cgi
import psycopg2

form = cgi.FieldStorage()

tin = form.getvalue('s_tin')
name = form.getvalue('s_name')
address = form.getvalue('s_address')
sku = form.getvalue('s_sku')
date = form.getvalue('s_date')

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

    sql = 'INSERT INTO supplier (TIN, name, address, sku, date) VALUES (%s, %s, %s, %s, %s)'
    # Execute the INSERT statement
    cursor.execute(sql, (tin, name, address, sku, date))
    print("<h1> Supplier registered with success</h1>")
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