def ingresarPaisPoblacion():
    pais=[]
    for x in range(5):
        nombre=input('Ingrese el nombre del país:')
        cantidad=int(input('Cantidad habitanes:'))
        pais.append((nombre,cantidad))
    return pais

def imprimir(paises):
    print('Paises y su Población:')
    for x in range(len(paises)):
        print(paises[x][0],paises[x][1])

def paismayorpoblacion(paises):
    pos=0
    for x in range (1,len(paises)):
        if (paises[x][1]>paises[pos][1]):
            pos=x
    print('Pais con mayor cantidad de habitantes:',paises[pos][0])
# principal
paises=ingresarPaisPoblacion()
imprimir(paises)
paismayorpoblacion(paises)
