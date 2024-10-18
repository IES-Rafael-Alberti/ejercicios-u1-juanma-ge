importe_sin_iva = float(input("Dime cuánto es el importe sin iva: "))

tipo_de_iva = float(input("Dime del tipo de iva: "))

iva = importe_sin_iva * (tipo_de_iva / 100)

precio_final = importe_sin_iva + iva

print(f"El precio final el producto son {precio_final: .2f} euros.")
