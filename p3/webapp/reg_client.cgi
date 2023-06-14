#!/usr/bin/python3
import cgi
import psycopg2

form = cgi.FieldStorage()

cust_no = form.getvalue('c_cust_no')
cust_name = form.getvalue('c_name')
cust_email = form.getvalue('c_email')
cust_phone = form.getvalue('c_phone')
cust_address = form.getvalue('c_address')

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

    if not (cust_no.isdigit() and cust_name.isalpha() and cust_phone.isdigit()):
        raise ValueError('customer number, phone, should be numeric values and name should be alphabetical.')

    # Creating connection
    connection = psycopg2.connect(dsn)
    print('<p>Connected<p>')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO customer VALUES (%s, %s, %s, %s, %s)', (cust_no,cust_name,cust_email,cust_phone,cust_address))
    print("<h1> Client registered with success</h1>")
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