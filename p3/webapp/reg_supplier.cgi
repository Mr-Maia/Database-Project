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
print('<title>DBgrupo34</title>')
print('<style>')
print('input[type="submit"] {')
print('    display: block;')
print('    width: 20%;')
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
    if not (tin.isdigit() and name.isalpha() and sku.isdigit()):
        print("<h1> TIN and SKU should be numeric values and the name should be alhpabetical</h1>")
        print("<form action='local.html'>")
        print("<input type='submit' value='Return to main menu'>")
        print('</form>')
        print('</body>')
        print('</html>')
        raise ValueError()
    # Creating connection
    connection = psycopg2.connect(dsn)
    print('<p>Connected<p>')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM supplier where TIN = %s', (tin,))
    supplier = cursor.fetchone()

    if supplier is not None:
        print('<h1><h1> There is already a supplier with that TIN</h1>')
        print("<form action='local.html'>")
        print("<input type='submit' value='Return to main menu'>")
        print('</form>')
        print('</body>')
        print('</html>')
        raise ValueError()

    sql = 'INSERT INTO supplier(TIN, NAME, ADDRESS, SKU, DATE) VALUES (%s, %s, %s, %s, %s)'
    # Execute the INSERT statement
    cursor.execute(sql, (tin, name, address, sku, date))
    print("<h1> Supplier registered with success</h1>")
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