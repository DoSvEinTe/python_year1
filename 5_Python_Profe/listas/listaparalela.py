nombres=[]
edades=[]

for x in range(5):
    nombre=input('Ingrese Nombre:')
    nombres.append(nombre)
    edad=int(input('Ingrese edad:'))
    edades.append(edad)

print('Nombre de las Personas Mayores de edad:')
for x in range(5):
    if edades[x]>=18:
        print('Nombre',nombres[x])

print('Lista de Nombres')
for x in range(5):
    print(nombres[x],edades[x])
