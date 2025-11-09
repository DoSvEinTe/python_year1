#diccionarios con valores de tipo lista, tuplas y diccionarios

def ingresar():
    productos={}
    continua='s'
    while continua=='s':
        codigo=int(input('Codigo Producto:'))
        descripcion=input('Descripción Producto:')
        precio=int(input('Precio Producto:'))
        stock=int(input('Ingrese Stock Actual:'))
        productos[codigo]=(descripcion,precio,stock)
        continua=input('Desear ingresar otro Producto [s/n] :')
    return productos

def imprimir(productos):
    print('LISTADO COMPLETO DE PRODUCTOS')
    for codigo in productos:
        print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])

def consulta(productos):
    codigo=int(input('Ingrese codigo Producto a Buscar:'))
    if codigo in productos:
       print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])

def listadoStockCero(productos):
    print('LISTADO PRODUCTOS CON STOCK 0')
    for codigo in productos:
        if productos[codigo][2]==0:
             print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])
#principal
productos=ingresar()
imprimir(productos)
consulta(productos)
listadoStockCero(productos)