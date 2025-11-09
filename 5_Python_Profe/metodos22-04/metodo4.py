def mostrar_mayor(v1,v2):
    if v1>v2:
        mayor=v1
    else:
        mayor=v2
    return mayor

#bloque principal 
valor1=int(input("Ingrese Valor 1:"))
valor2=int(input("Ingrese Valor 2:"))
print("El mayor es:",mostrar_mayor(valor1,valor2))

