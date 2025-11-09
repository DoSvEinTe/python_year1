def ingresar():
    diccionario = {}
    continuar = "s"
    while continuar == "s":
        caste = input("Ingrese una palabra castellano: ")
        ing = input("Ingrese palabra en ingles: ")
        diccionario[ing]=caste
        continuar=input("Desea continuar ingresando [s/n]: ")
    return diccionario

def imprimir(diccionario):
    print("Listado completo del diccionario: ")
    for ingles in diccionario:
        print(ingles, diccionario[ingles])

def consulta_palabra(diccionario):
    palabra = input("Ingrese una palabra en ingles para continuar: ")
    if palabra in diccionario:
        print(f"En castellano significa: {diccionario[palabra]}")

# PRINCIPAL
diccionario=ingresar()
imprimir(diccionario)
consulta_palabra(diccionario)