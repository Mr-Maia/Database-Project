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

    # Validating SKU, EAN, and price as numeric values
    if not (sku.isdigit() and ean.isdigit() and name.isalpha() and price.replace('.', '', 1).isdigit()):
        print("<h1>'SKU, EAN, and price should be numeric values and the name should be alphabetical.</h1>'")
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

    cursor.execute('SELECT * FROM product where SKU = %s', (sku,))
    product = cursor.fetchone()
    if product is not None:
        print('<h1>There is already a product with that sku</h1>')
        print("<form action='local.html'>")
        print("<input type='submit' value='Return to main menu'>")
        print('</form>')
        print('</body>')
        print('</html>')
        raise ValueError()

    sql = 'INSERT INTO product (SKU, name, description, price, ean) VALUES (%s, %s, %s, %s, %s)'
    # Execute the INSERT statement
    cursor.execute(sql, (sku, name, description, price, ean))
    print("<h1> Product registered with success</h1>")
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