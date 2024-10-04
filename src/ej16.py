barras_otro_dia = int(input("¿Qué número de barras se venden y no son del día?: "))
precio_pan = 3.49

descuento = (3.49 * 60)/100

coste = precio_pan - descuento

coste_final = coste * barras_otro_dia

print(f"Las barras de pan con descuento valen {descuento} euros y su coste final es de {coste_final: .2f} euros.")