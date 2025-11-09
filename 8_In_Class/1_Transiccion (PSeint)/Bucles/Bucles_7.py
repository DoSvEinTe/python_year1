cant = 0
x = 1
n = int(input("Cuantas piezas cargara: "))

while x <= n: #Definde hasta cuando dura el ciclo, empieza desde el 1 hasta n
    largo = float(input("Ingrese la medida de la pieza: ")) #Pregunta un parametro (largo)
    if largo >= 1.2 and largo <= 1.3: #Si el largo esta o es 1.2 o 1.3 contara la cantidad
         cant = cant + 1  #contar cantidades
    x += 1 #Acumulador para terminar el ciclo

print("La cantidad de piezas", cant)

#Ciclo que pregunta cuantas veces se repetira y por medio del if, ira contando la cantidades de piezas que segun un parametro se ira acumulando
