#!/usr/bin/python3
import cgi
import psycopg2

form = cgi.FieldStorage()

tin = form.getvalue('s_tin')

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
    if not (tin.isdigit()):
        raise ValueError('TIN should be numeric values.')
    # Creating connection
    connection = psycopg2.connect(dsn)
    print('<p>Connected<p>')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM supplier where TIN = %s', (tin,))
    supplier = cursor.fetchone()

    if supplier is None:
        print("<h1> There is no supplier with that TIN")

    cursor.execute('DELETE FROM supplier WHERE TIN = %s', (tin,))
    print("<h1> Supplier removed with success</h1>")
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