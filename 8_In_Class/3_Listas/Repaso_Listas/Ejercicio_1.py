lista = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
 #         0         1         2

# IMPRIMIR LISTA COMPLETA
print("___________________________________________________________________")
print("IMPRIMIR LA LISTA COMPLETA:")
print(lista)
print("___________________________________________________________________")
print("IMPRIME EL PRIMER COMPONENTE:")
print(lista[0])
print("___________________________________________________________________")
print("IMPRIMIR EL PRIMER COMPONENTE CONTENIDO DE LA LISTA:")
print(lista[0][0])
print(lista[1][0])
print(lista[2][2])
# print(lista[2][3]) -----> # NUM 3 FUERA DE RANGO, SALDRIÁ ERROR
print("____________________________________________________________________")
print("IMPRIMIR UN FOR LA LISTA CONTENIDOS EN EL PRIMER DE LA LISTA:")
for x in range(len(lista)):
    print(lista[2][x])
print("____________________________________________________________________")