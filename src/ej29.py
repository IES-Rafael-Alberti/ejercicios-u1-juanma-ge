def leer_nombre():
    nombre = input("Dime tu nombre: ")
    if not nombre:
        nombre = "Desconocido"
    return nombre

def leer_edad():
    while True:
        edad = int(input("Dime tu edad: "))
        if 0 <= edad <= 125:
            return edad
        else:
            print("La edad debe estar entre los 0 y los 125 años. Inténtalo de nuevo.")

def main():
    nombre = leer_nombre()
    edad = leer_edad()
    años_faltantes = 125 - edad
    print(f"Te llamas {nombre}, tienes {edad} años y te faltan {años_faltantes} años por cumplir.")

main()