#!/usr/bin/env python
import cgi
import cgitb
import psycopg2


def connect_sigma():
    conn = psycopg2.connect(database="your_database", user="your_user", password="your_password", host="your_host", port="your_port")

# Função para registrar o produto no banco de dados
def register_product(sku, name, description, price, ean):
    # Coloque aqui o código para inserir os dados no banco de dados
def remove_product(sku):

def register_supplier(tin, name, address, sku, date):

def remove_supplier(tin):


def main():
    # Obtém os dados enviados pelo formulário
    form = cgi.FieldStorage()
    action = form.getvalue('action')

    if action == 'register_product':
        # Obtém os valores dos campos do formulário
        sku = form.getvalue('sku')
        name = form.getvalue('name')
        description = form.getvalue('description')
        price = form.getvalue('price')
        ean = form.getvalue('ean')
        
        # Chama a função para registrar o produto
        register_product(sku, name, description, price, ean)
        
        # Redireciona o usuário para uma página de confirmação
        print("Content-Type: text/html")
        print()
        print("<h1>Product registered with success!</h1>")

    elif action == 'remove_product':
        # Gets the data:
        sku = form.getvalue('sku')
        # Calls the function:
        remove_product(sku)
        # Confirms the success:
        print("Content-Type: text/html")
        print()
        print("<h1>Product removed with success!</h1>")

    elif action == 'register_supplier':
        # Gets the data:
        tin = form.getvalue('tin')
        name = form.getvalue('name')
        address = form.getvalue('address')
        sku = form.getvalue('sku')
        date = form.getvalue('date')
        # Calls the function:
        register_supplier(tin, name, address, sku, date)
        # Confirms the success:
        print("Content-Type: text/html")
        print()
        print("<h1>Supplier registered with success!</h1>")

    elif action == 'remove_supplier':
        # Gets the data:
        tin = form.getvalue('tin')
        # Calls the function:
        remove_supplier(tin)
        # Confirms the success:
        print("Content-Type: text/html")
        print()
        print("<h1>Supplier removed with success!</h1>")


    else:
        # Ação inválida
        print("Content-Type: text/html")
        print()
        print("<h1>Ação inválida</h1>")

# Chama a função principal
if __name__ == '__main__':
    main()
