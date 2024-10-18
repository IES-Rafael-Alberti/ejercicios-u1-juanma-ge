correo = input("Escribe el correo del usuario: ")

pos_arroba = correo.find("@")

print(f"{correo[:pos_arroba] + "@ceu.es"}")