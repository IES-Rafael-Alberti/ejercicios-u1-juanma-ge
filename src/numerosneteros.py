
def comprobar_entero(cadena : str) -> bool:
    cadena = cadena.strip()
    return cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit)

def dame_entero() -> int: 
    cadena = input("Dame un entero: ")
    while not comprobar_entero(cadena):
       cadena = input("\n**ERROR** no es un entero\n\nDame un entero de verdad: ")


def main(): 
    num = dame_entero()
    print(f"Escribste el número {num}")


if __name__ == "__main__": 
    main()