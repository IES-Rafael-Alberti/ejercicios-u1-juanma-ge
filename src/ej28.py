def leer_numeros():
    num1 = int(input("Dime un número entero: "))
    num2 = int(input("Dime otro número entero: "))
    
    if num1 == num2:
        print("Los números no pueden ser iguales")
    else:
         return num1, num2


def encontrar_menor(num1, num2): 
    if num1 < num2:
        return num1
    else: 
        return num2

def contar_numeros(num1, num2):
    return abs(num1 - num2)

def main():
        num1, num2 = leer_numeros()
        if num1 is None or num2 is None:
            return
        numeros = contar_numeros(num1, num2)
        menor = encontrar_menor(num1, num2)
        print(f"El número menor es el {menor} y entre ellos hay {numeros} números.")

main()