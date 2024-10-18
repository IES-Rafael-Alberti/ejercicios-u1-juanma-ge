def saludar(nombre):
    return (f"Hola, {nombre}.")

def main():
    nombre = input("Dime como te llamas: ")
    mensaje = saludar (nombre)
    print(mensaje)

if __name__ == "__main__":
    main()