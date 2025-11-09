n1=float(input("Ingrese Nota 1"))
n2=float(input("Ingrese Nota 2"))
n3=float(input("Ingrese Nota 3"))
promedio=(n1+n2+n3)/3

if promedio>=4 and promedio<5:
    print(promedio,"Nota Suficiente")
    if (promedio>=5 and promedio<6):
        print(promedio,"Nota Bueno")
    else:
        if(promedio>=6 and promedio<=7):
            print(promedio,"Nota excelente")
else:
    print(promedio,"Nota Insuficiente")
