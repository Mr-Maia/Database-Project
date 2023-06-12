#!/usr/bin/env python3
import cgi

print("Content-type: text/html\n\n")
print(f"""\
<!DOCTYPE html>
<html lang="n">
<head>
    <meta charset="UTF-8">
    <title>Gerenciamento de Produtos e Fornecedores</title>
</head>
<body>
    <h1>Xingui Ling's Store</h1>

    <h2>Register Product</h2>
        <input type="hidden" name="action" value="register_product">
        SKU: <input type="text" name="sku"><br>
        Nome: <input type="text" name="name"><br>
        Descrição: <input type="text" name="description"><br>
        Preço: <input type="text" name="price"><br>
        EAN: <input type="text" name="ean"><br>
        <input type="submit" value="Register Product">
    </form>

    <h2>Remove Product</h2>
        <input type="hidden" name="action" value="remove_product">
        SKU: <input type="text" name="sku"><br>
        <input type="submit" value="Remove Product">
    </form>

    <h2>Registo de Fornecedor</h2>
        <input type="hidden" name="action" value="register_supplier">
        TIN: <input type="text" name="tin"><br>
        Nome: <input type="text" name="name"><br>
        Endereço: <input type="text" name="address"><br>
        SKU: <input type="text" name="sku"><br>
        Data: <input type="text" name="date"><br>
        <input type="submit" value="Register Supplier">
    </form>

    <h2>Remoção de Fornecedor</h2>
        <input type="hidden" name="action" value="remove_supplier">
        TIN: <input type="text" name="tin"><br>
        <input type="submit" value="Remove Supplier">
    </form>
</body>
</html>
""")
