lista = [20, 30, 7, 3, 2]

#En este caso el modulo len(lista) devolveria 5 elementos

i = 0
acum = 0
print("")
while i < len(lista):

#Mientras i = 0 sea menor a len(lista) = 5 el ciclo while se repetira
    
    print("Lista : ", lista[i])
    print("Acumulador: ", acum)

    acum = acum + lista [i] 

#Contador para terminar el ciclo en algun momento y evitar crear un ciclo infinito
    
    i = i + 1
    
print("")
print("Contenidos de la lista: ", lista)
print("La suma de sus elementos es: ", acum)
print("")