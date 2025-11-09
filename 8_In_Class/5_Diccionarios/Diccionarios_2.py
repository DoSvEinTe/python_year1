def ingresar():
    productos = {}
    for x in range(5):
        nombre = input("Nombre producto: ")
        precio = int(input("Precio producto: "))
        productos[nombre] = precio
    return productos

def imprimir(productos):
    print("Listado de todos los articulos")
    for nombre in productos:
        print(nombre, productos[nombre])

def imprimir_mayor1000(productos):
    print("Listado de productos con precio >= 1000")
    for nombre in productos:
        if productos[nombre] >= 1000:
            print(nombre)
    
# BLOQUE PRINCIPAL
productos = ingresar()
imprimir(productos)
imprimir_mayor1000(productos)