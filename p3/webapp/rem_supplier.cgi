#!/usr/bin/python3
import cgi
import psycopg2
import configparser

form = cgi.FieldStorage()

tin = form.getvalue('s_tin')

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
    if not (tin.isdigit()):
        print("<h1> TIN should be numeric values.</h1>")
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

    if supplier is None:
        print('<h1><h1> No supplier found</h1>')
        print('<p>There is no supplier with that TIN</p>')
        print("<form action='local.html'>")
        print("<input type='submit' value='Return to main menu'>")
        print('</form>')
        print('</body>')
        print('</html>')
        raise ValueError()

    cursor.execute('DELETE FROM supplier WHERE TIN = %s', (tin,))
    print("<h1> Supplier removed with success</h1>")
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