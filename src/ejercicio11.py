num = int(input("Escribe un número entero a tu elección: "))

while num<1:
    print("ERROR")
    num  = int(print("Escribe otro número: "))


suma = (num * (num + 1))/2

print(f"El total de la operación es {suma}")