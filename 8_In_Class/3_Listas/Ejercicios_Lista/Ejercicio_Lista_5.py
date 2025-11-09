#Listas paralelas
nombres = []
edades = []

#Se ingresa el nombre y edad de cada persona
for x in range(5):
    nombre = input("Ingrese su nombre: ")
    nombres.append(nombre)
    edad = int(input("Ingrese su edad: "))
    edades.append(edad)

print("")

#Se imprime las personas que son mayores de edad segun un ciclo for
print("Nombre de las personas mayores de edad: \n")
for x in range(5):
    if edades[x] >= 18:
        print(f"- {nombres[x]}")

print("")

#Se imprime la lista completa y la edad de cada persona
for x in range(5):
    print(f"{nombres[x]} tiene {edades[x]} años")

print("")