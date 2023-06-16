#!/usr/bin/python3
import cgi
import psycopg2
import configparser

form = cgi.FieldStorage()

cust_no = form.getvalue('c_cust_no')
cust_name = form.getvalue('c_name')
cust_email = form.getvalue('c_email')
cust_phone = form.getvalue('c_phone')
cust_address = form.getvalue('c_address')

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
print('body {')
print('  font-family: Arial, sans-serif;')
print('  margin: 0;')
print('  padding: 20px;')
print('  background-color: #FFF7ED;')
print('}')
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

# Adding SVG
print('<div class="logo">')
print('<svg width="562.25" height="123.62471194983922" viewBox="0 0 370.0169491525424 81.35747221972674" class="css-1j8o68f"><defs id="SvgjsDefs1644"></defs><g id="SvgjsG1645" featurekey="4K7G0D-0" transform="matrix(1.8511347428023217,0,0,1.8511347428023217,0.05840180720494287,-3.7022694856046434)" fill="#ff325d"><title xmlns="http://www.w3.org/2000/svg">e commerce_26</title><path xmlns="http://www.w3.org/2000/svg" d="M48,20.75A25,25,0,0,0,24,2,25,25,0,0,0,0,20.75a1,1,0,0,0,1.94.5A23.23,23.23,0,0,1,5.6,13.57,39,39,0,0,0,14.87,16c-.52,2-1,4-1.3,6H10a4,4,0,0,0-.93,7.88,85.6,85.6,0,0,0,2,13.07,4.26,4.26,0,0,0,4.09,3H32.82a4.26,4.26,0,0,0,4.09-3,85.6,85.6,0,0,0,2-13.07A4,4,0,0,0,38,22H34.43c-.34-1.94-.78-4-1.3-6a39,39,0,0,0,9.27-2.46A23.23,23.23,0,0,1,46,21.25,1,1,0,0,0,47,22a1.07,1.07,0,0,0,.25,0A1,1,0,0,0,48,20.75ZM30.6,14.35a63.94,63.94,0,0,1-6.6.36,61.22,61.22,0,0,1-6.6-.37C19.28,8.22,21.8,4,24,4S28.72,8.22,30.6,14.35ZM6.88,11.94A22.81,22.81,0,0,1,19.94,4.38c-1.84,2.24-3.36,5.82-4.52,9.72A38.4,38.4,0,0,1,6.88,11.94ZM35,42.4A2.25,2.25,0,0,1,32.82,44H15.18A2.25,2.25,0,0,1,13,42.4,82.92,82.92,0,0,1,11.09,30H36.91A82.92,82.92,0,0,1,35,42.4ZM38,24a2,2,0,0,1,0,4H10a2,2,0,0,1,0-4h3.25q-.13,1-.24,1.89a1,1,0,0,0,2,.22c.09-.71.18-1.41.28-2.11H32.73c.1.7.19,1.4.28,2.11A1,1,0,0,0,34,27h.11a1,1,0,0,0,.88-1.1q-.1-.91-.24-1.89Zm-5.59-2H15.59c.35-2,.77-3.91,1.25-5.71a61.52,61.52,0,0,0,7.16.42,61.52,61.52,0,0,0,7.16-.42C31.64,18.09,32.06,20,32.41,22Zm.17-7.9c-1.16-3.9-2.68-7.48-4.52-9.72a22.81,22.81,0,0,1,13.06,7.56A38.4,38.4,0,0,1,32.58,14.1ZM17.49,33.84l1,6A1,1,0,0,1,17.66,41H17.5a1,1,0,0,1-1-.84l-1-6a1,1,0,1,1,2-.32Zm15,.32-1,6a1,1,0,0,1-1,.84h-.16a1,1,0,0,1-.83-1.15l1-6a1,1,0,0,1,2,.32ZM25,34v6a1,1,0,0,1-2,0V34a1,1,0,0,1,2,0Z"></path></g><g id="SvgjsG1646" featurekey="wPuqcM-0" transform="matrix(2.194526179542731,0,0,2.194526179542731,106.366570049553,7.832847108470121)" fill="#ff325d"><path d="M6.2 6 c3.98 0 7.1 3.12 7.1 6.92 c0 3.96 -3.12 7.08 -7.1 7.08 l-5 0 l0 -14 l5 0 z M6.18 17.240000000000002 c2.68 0 4.12 -1.94 4.12 -4.32 c0 -2.22 -1.44 -4.16 -4.12 -4.16 l-2.06 0 l0 8.48 l2.06 0 z M23.02 12.24 c1.48 0.4 2.88 1.72 2.88 3.66 c0 2.54 -1.6 4.1 -5.08 4.1 l-5.52 0 l0 -14 l5.22 0 c2.9 0 4.36 1.64 4.36 3.52 c0 1.48 -0.96 2.32 -1.86 2.72 z M20.24 8.56 l-2.02 0 l0 2.82 l2.02 0 c1.24 0 1.74 -0.58 1.74 -1.42 c0 -0.9 -0.58 -1.4 -1.74 -1.4 z M20.66 17.44 c1.6 0 2.32 -0.66 2.32 -1.9 c0 -1.06 -0.72 -1.8 -2.44 -1.8 l-2.32 0 l0 3.7 l2.44 0 z M41.32 9.6 l2.86 0 l0 10.4 c0 3.16 -3.1 4.12 -5.36 4.12 c-1.2 0 -2.2 -0.24 -2.82 -0.58 l0 -2.34 c0.62 0.34 1.58 0.54 2.82 0.54 c1.84 0 2.5 -0.98 2.5 -1.74 l0 -1.28 c-0.06 0.42 -1.08 1.48 -2.88 1.48 c-2.38 0 -5.14 -1.72 -5.14 -5.42 c0 -3.58 2.76 -5.36 5.14 -5.36 c1.8 0 2.82 1.12 2.88 1.34 l0 -1.16 z M38.84 17.66 c1.4 0 2.62 -0.96 2.62 -2.88 c0 -1.86 -1.22 -2.82 -2.62 -2.82 c-1.44 0 -2.76 0.98 -2.76 2.82 c0 1.9 1.32 2.88 2.76 2.88 z M52.72 9.44 c0.26 0 0.5 0 0.76 0.06 l0 2.74 c-0.24 -0.06 -0.48 -0.06 -0.68 -0.06 c-1.92 0 -3.5 1.38 -3.68 3.38 l0 4.44 l-2.86 0 l0 -10.4 l2.86 0 l0 2.6 c0.46 -1.58 1.72 -2.76 3.6 -2.76 z M60.239999999999995 9.42 c2.36 0 5.44 1.78 5.44 5.42 s-3.08 5.36 -5.44 5.36 s-5.46 -1.72 -5.46 -5.36 s3.1 -5.42 5.46 -5.42 z M60.239999999999995 11.96 c-1.3 0 -2.68 0.98 -2.68 2.88 c0 1.84 1.38 2.82 2.68 2.82 c1.28 0 2.68 -0.98 2.68 -2.82 c0 -1.9 -1.4 -2.88 -2.68 -2.88 z M71.22 20.16 c-1.98 0 -3.94 -1.3 -3.94 -4.58 l0 -5.98 l2.86 0 l0 5.78 c0 1.7 0.66 2.28 1.76 2.28 c1.52 0 2.42 -1.44 2.64 -2.16 l0 -5.9 l2.86 0 l0 10.4 l-2.86 0 l0 -1.92 c-0.2 0.54 -1.32 2.08 -3.32 2.08 z M85.22 9.42 c2.38 0 5.14 1.78 5.14 5.36 c0 3.7 -2.76 5.42 -5.14 5.42 c-1.8 0 -2.82 -1.06 -2.88 -1.48 l0 5.08 l-2.86 0 l0 -6.12 l0 -8.08 l2.86 0 l0 1.16 c0.06 -0.22 1.08 -1.34 2.88 -1.34 z M84.82 17.66 c1.44 0 2.76 -0.98 2.76 -2.88 c0 -1.84 -1.32 -2.82 -2.76 -2.82 c-1.4 0 -2.62 0.96 -2.62 2.82 c0 1.92 1.22 2.88 2.62 2.88 z M100.08 15.82 c0.66 1.3 1.66 1.88 2.72 1.88 c0.8 0 2.4 -0.36 2.4 -2.38 c0 -1.72 -1.62 -2.9 -4.32 -2.18 l2.74 -4.64 l-5.12 0 l0 -2.5 l9.26 0 l-3.14 5.16 c1.92 0.28 3.5 1.98 3.5 4.16 c0 3.1 -2.42 4.88 -5.36 4.88 c-2.36 0 -4.1 -1.28 -4.9 -3.04 z M120.14 14.4 l0 2.5 l-1.5 0 l0 3.1 l-2.92 0 l0 -3.1 l-6 0 l0 -2.5 l6 -8.4 l2.92 0 l0 8.4 l1.5 0 z M112.72 14.4 l3 0 l0 -4.48 z"></path></g></svg>')
print('</div>') 

connection = None

try:

    if not (cust_no.isdigit() and cust_name.isalpha() and cust_phone.isdigit()):
        print("<h1> customer number, phone, should be numeric values and name should be alphabetical.</h1>")
        print("<form action='local.html'>")
        print("<input type='submit' value='Return to main menu'>")
        print('</form>')
        print('</body>')
        print('</html>')
        raise ValueError()

    # Creating connection
    connection = psycopg2.connect(dsn)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM customer WHERE email = %s', (cust_email,))
    email = cursor.fetchone()

    if email is not None:
        print("<h1> Email is already in use</h1>")
        print("<form action='local.html'>")
        print("<input type='submit' value='Return to main menu'>")
        print('</form>')
        print('</body>')
        print('</html>')

    cursor.execute('SELECT * FROM customer WHERE phone = %s', (cust_phone,))
    phone = cursor.fetchone()

    if phone is not None:
        print("<h1> phone is already in use</h1>")
        print("<form action='local.html'>")
        print("<input type='submit' value='Return to main menu'>")
        print('</form>')
        print('</body>')
        print('</html>')


    cursor.execute('SELECT * FROM customer WHERE cust_no = %s', (cust_no,))
    customer = cursor.fetchone()

    if customer is not None:
        print("<h1> ERROR: There is already a client with that customer number</h1>")
        print("<form action='local.html'>")
        print("<input type='submit' value='Return to main menu'>")
        print('</form>')
        print('</body>')
        print('</html>')
        raise ValueError()

    cursor.execute('INSERT INTO customer (cust_no,name,email,phone,address) VALUES (%s, %s, %s, %s, %s)', (cust_no,cust_name,cust_email,cust_phone,cust_address))
    print("<h1> Client registered with success</h1>")
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