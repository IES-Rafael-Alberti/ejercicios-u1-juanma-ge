dinero = float(input("Dime la cantidad de dinero en la cuenta de ahorros: "))

pago_1_año = dinero * (1 + 4/100)
pago_2_año  = pago_1_año * (1 + 4/100)
pago_3_año = pago_2_año * (1 + 4/100)

print(f"La cantidad el primer año sería de {pago_1_año: .2f} euros, el segundo año de {pago_2_año: .2f} euros y el tercer año de {pago_3_año: .2f} euros.")