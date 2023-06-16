#!/usr/bin/python3
import cgi
import psycopg2
import configparser

form = cgi.FieldStorage()

sku = form.getvalue('p_sku')
price = form.getvalue('new_price')

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
    if not (sku.isdigit() and price.replace('.', '', 1).isdigit()):
        print("<h1>SKU/Price should be numeric values.")
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

    cursor.execute("SELECT * FROM product WHERE SKU = %s", (sku,))
    check_product = cursor.fetchone()
    if check_product is None:
        print("<h1>ERROR: There is no product with that sku")
        print("<form action='local.html'>")
        print("<input type='submit' value='Return to main menu'>")
        print('</form>')
        print('</body>')
        print('</html>')
        raise ValueError()
        pass

    cursor.execute('UPDATE product SET price = %s WHERE SKU = %s', (price, sku))
    connection.commit()
    print("<h1>Price changed with success!</h1>")
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