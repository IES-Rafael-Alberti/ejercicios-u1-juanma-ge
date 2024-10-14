import math

def calcular_semiperimetro(a, b, c):
    return (a + b + c)/2

def calcular_area(a, b, c):
    s = calcular_semiperimetro(a, b, c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = float(input("Escribe las medidas del lado a en cm: "))
b = float(input("Escribe las medidas del lado b en cm: "))
c = float(input("Escribe las medidas del lado c en cm: "))

area = calcular_area(a, b, c)
print(f"El area del triangulo son {area:.2f} cm")
