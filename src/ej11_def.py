def pedir_numero():
    num = int(input("Escribe un número entero a tu elección: "))
    return num


def validar_numero(num):
    while num<1:
        print("ERROR")
        num  = int(print("Escribe otro número: "))
    return num

def cuenta(num):
    return (num * (num + 1))/2

def main(): 
    num = pedir_numero()
    num = validar_numero(num)
    suma = cuenta(num)
    print(f"El total de la cuenta es {suma:.2f}")

main()