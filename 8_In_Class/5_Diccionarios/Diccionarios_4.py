# DICCIONARIO CON VALORES DE TIPO LISTA, TUPLAS Y DICCIONARIOS.

def ingresar():
    productos = {}
    continua = "s"
    while continua == "s":
        codigo = int(input("Codigo producto: "))
        descripcion = input("Descripcion producto: ")
        precio = int(input("Precio producto: "))
        stock = int(input("Ingrese stock actual: "))
        productos[codigo] = (descripcion, precio, stock)
        continua = input("desea ingresar otro producto?[s/n]: ")
    return productos

def imprimir(productos):
    print("Listado completo productos: ")
    for codigo in productos:
        print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2])

def consulta(productos):
    codigo = int(input("Ingrese codigo de producto a buscar: "))
    if codigo in productos:
        print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2])

def listado_stockcero(productos):
    print("Listado productos con stock 0")
    for codigo in productos:
        if productos[codigo][2]==0:
            print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2])

# PRINCIPAL
productos = ingresar()
imprimir(productos)
consulta(productos)
listado_stockcero(productos)