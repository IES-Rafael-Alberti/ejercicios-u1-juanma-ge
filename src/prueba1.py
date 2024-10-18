def comprobar_numero(num1, num2):
    if num1 > num2:
        return num1
    if num2 > num1:
        return num2
    if num1 == num2:
        return 0

def main():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = comprobar_numero(num1, num2)
    if resultado == 0:
        print("Los números son iguales.")
    else:
        print(resultado)
        
if __name__ == "__main__":
    main()