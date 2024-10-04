#
p = int(input("Escribe el número de payasos vendidos: "))
m = int(input("Escribe el número de muñecas vendidas: "))

pesop = 112 * p
pesom = 75 * m

kgp = pesop / 1000
kgm =  pesom / 1000
kg = kgp + kgm 

print(f"El peso total es de {kg} kg.")
