def calcular_celsius(farenheit: float) -> float:
    celsius = (5 / 9) * (farenheit - 32)
    return celsius

def main():
     farenheit = float(input("Introduce los grados Fahrenheit: "))
     celsius = calcular_celsius(farenheit)
     print(f"{farenheit} grados Fahrenheit son {celsius: .2f} grados Celsius")

if __name__ == "__main__":
    main()