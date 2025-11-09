def ver_mayor(v1,v2,v3):
    
    if v1 > v2 and v1 > v3:
        mayor = v1
    elif v2 > v3:
        mayor = v2
    else:
        mayor = v3
    return mayor

def ingresar():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el Segundo valor: "))
    valor3 = int(input("Ingrese el Tercero valor: "))
    mostrar = ver_mayor(valor1,valor2,valor3)
    print("El mayor de los 3 numeros es:",mostrar)

#bloque principal
ingresar()