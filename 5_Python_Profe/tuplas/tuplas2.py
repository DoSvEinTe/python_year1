def ingresarFecha():
    d=int(input('Ingresar Día:'))
    m=int(input('Ingresar Mes:'))
    a=int(input('Ingresar Año:'))
    return (d,m,a)

def imprimirFecha(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")

#principal
fecha=ingresarFecha()
imprimirFecha(fecha)    