#!/usr/bin/env python3
print(f"""\n
<html>
<head>
    <meta charset="UTF-8">
    <title>Gerenciamento de Produtos e Fornecedores</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f3f3f3;
            margin: 0;
            padding: 20px;
        }

        h1 {
            font-size: 24px;
            color: #333;
            margin-bottom: 20px;
        }

        h2 {
            font-size: 20px;
            color: #333;
            margin-bottom: 10px;
        }

        form {
            background-color: #fff;
            padding: 20px;
            border-radius: 4px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        input[type="text"],
        input[type="submit"] {
            display: block;
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            font-size: 14px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        input[type="submit"] {
            background-color: #f0c14b;
            color: #333;
            font-weight: bold;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #d89e35;
        }
    </style>
</head>
<body>
    <h1>Xingui Ling's Store</h1>

    <h2>Register Product</h2>
    <form action="reg_product.py" method="post">
        <input type="hidden" name="action" value="register_product">
        <input type="text" name="p_sku" placeholder="SKU">
        <input type="text" name="p_name" placeholder="Nome">
        <input type="text" name="p_description" placeholder="Descrição">
        <input type="text" name="p_price" placeholder="Preço">
        <input type="text" name="p_ean" placeholder="EAN">
        <input type="submit" value="Register Product">
    </form>

    <h2>Remove Product</h2>
    <form action="script.py" method="post">
        <input type="hidden" name="action" value="remove_product">
        <input type="text" name="p_sku" placeholder="SKU">
        <input type="submit" value="Remove Product">
    </form>

    <h2>Alterar preços de produtos e respectivas descrições</h2>
    <form action="script.py" method="post">
        <input type="hidden" name="action" value="alter_product">
        <input type="text" name="p_sku" placeholder="SKU">
        <input type="text" name="new_price" placeholder="Novo Preço">
        <input type="text" name="new_description" placeholder="Nova Descrição">
        <input type="submit" value="Alter Product">
    </form>

    <h2>Registar Cliente</h2>
    <form action="script.py" method="post">
        <input type="hidden" name="action" value="register_customer">
        <input type="text" name="c_cust_no" placeholder="Número do Cliente">
        <input type="text" name="c_name" placeholder="Nome">
        <input type="text" name="c_email" placeholder="Email">
        <input type="text" name="c_phone" placeholder="Telefone">
        <input type="text" name="c_address" placeholder="Endereço">
        <input type="submit" value="Register Customer">
    </form>

    <h2>Remover Cliente</h2>
    <form action="script.py" method="post">
        <input type="hidden" name="action" value="remove_customer">
        <input type="text" name="c_cust_no" placeholder="Número do Cliente">
        <input type="submit" value="Remove Customer">
    </form>

    <h2>Registar Fornecedor</h2>
    <form action="script.py" method="post">
        <input type="hidden" name="action" value="register_supplier">
        <input type="text" name="s_tin" placeholder="TIN">
        <input type="text" name="s_name" placeholder="Nome">
        <input type="text" name="s_address" placeholder="Endereço">
        <input type="text" name="s_sku" placeholder="SKU">
        <input type="text" name="s_date" placeholder="Data">
        <input type="submit" value="Register Supplier">
    </form>

    <h2>Remover Fornecedor</h2>
    <form action="script.py" method="post">
        <input type="hidden" name="action" value="remove_supplier">
        <input type="text" name="s_tin" placeholder="TIN">
        <input type="submit" value="Remove Supplier">
    </form>

    <h2>Realizar Encomenda</h2>
    <form action="script.py" method="post">
        <input type="hidden" name="action" value="place_order">
        <input type="text" name="o_order_no" placeholder="Número da Encomenda">
        <input type="text" name="o_cust_no" placeholder="Número do Cliente">
        <input type="text" name="o_date" placeholder="Data">
        <input type="submit" value="Place Order">
    </form>

    <h2>Simular Pagamento de Encomenda</h2>
    <form action="script.py" method="post">
        <input type="hidden" name="action" value="simulate_payment">
        <input type="text" name="p_order_no" placeholder="Número da Encomenda">
        <input type="text" name="p_cust_no" placeholder="Número do Cliente">
        <input type="submit" value="Simulate Payment">
    </form>
</body>
</html>
""")