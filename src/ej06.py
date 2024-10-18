importe_final = float(input("Dime el importe final del artículo: "))
 
tipo_de_iva = 10/100

iva_pagado = importe_final * tipo_de_iva

importe_sin_iva = importe_final - iva_pagado

print(f"El precio del iva pagado son {iva_pagado: .2f} euros y el importe sin iva son {importe_sin_iva: .2f} euros.")