precio = float(input("Escribe el precio del producto en euros y con dos decimales: "))
eur = precio.find(".")

print(f"{eur[:eur]}")