def convertir_temperatura(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)


fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
celsius = convertir_temperatura(fahrenheit)
print(f"La temperatura en celsius es de {celsius:.2f}ºC, cuando en farenheit eran {fahrenheit:.2f}ºF.")
