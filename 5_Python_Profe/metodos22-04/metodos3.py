#uso de función con retorno
#obtener la superficio de un cuadrado

def call_superficie(lado):
    sup=lado*lado
    return sup

#bloque principal para la llamada a metodo
lado=int(input("Ingrese lado del cuadrado:"))
superficie=call_superficie(lado)
print("La superficie del cuadrado es:",superficie)



