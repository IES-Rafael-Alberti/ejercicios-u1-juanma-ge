precio = input("Escribe el precio del producto en euros y con dos decimales: ")

eur = precio.find(".")
cent = precio.find(".")

print("Los euros totales son: ", precio[:eur], "y los céntimos totales serían: ", precio[cent:])