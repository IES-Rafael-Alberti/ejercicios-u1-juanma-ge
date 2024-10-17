def calcular_precio_con_iva(precio_sin_iva, tipo_iva):
    iva = precio_sin_iva * (tipo_iva/100)
    precio_final = precio_sin_iva + iva
    print(f"El precio final son {precio_final} euros.")


def main():
    precio_sin_iva = float(input("Dime el precio del producto sin iva: "))
    tipo_iva = float(input("Dime el tipo de iva: "))
    calcular_precio_con_iva(precio_sin_iva, tipo_iva)

main()