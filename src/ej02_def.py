def calcular_importe(horas, coste):
    return horas * coste

horas = input("¿Cuántas horas trabaja?")
coste = input("¿Y cuál es su coste?")
importe = calcular_importe(horas, coste)
print(f"El importe total son {importe}.")
