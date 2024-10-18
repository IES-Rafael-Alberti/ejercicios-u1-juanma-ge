productos = input("Escribe todos los productos de una cesta de la compra, separados por comas: ")

lista = productos.split(",")

for productos in lista:
    print(productos)