def calcular_precio(importe: float, iva: float) -> float:
    if iva < 0 or iva > 100:
        iva = 21
    precio_total = importe + ((importe * iva) / 100)
    return precio_total

def main():
    importe = float(input("Dime el importe: "))
    iva = float(input("Dime el iva del producto: "))
    precio = calcular_precio(importe, iva)
    print(f"{precio}")

main()