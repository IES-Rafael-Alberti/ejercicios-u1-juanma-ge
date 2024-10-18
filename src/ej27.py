nombre = input("Escribe el nombre del producto: ")
precio = float(input("Escribe el precio del producto: "))
unidades = int(input("Escribe el número de unidades: "))

coste = precio * unidades

print(f"El nombre del producto es {nombre}, su precio unitario es de {precio:09.2f} euros y su coste total de {coste:011.2f} euros.")