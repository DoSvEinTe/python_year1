def ingresar():
    diccionario={}
    continuar='s'
    while continuar=='s':
        caste=input('Ingrese Palabra Castellano:')
        ing=input('Ingrese Palabra en Ingles:')
        diccionario[ing]=caste
        continuar=input('Desea continuar ingresando:[s/n]')
    return diccionario

def imprimir(diccionario):
    print('Listado completo del diccionario:')
    for ingles in diccionario:
        print(ingles,diccionario[ingles])

def consultaPalabra(diccionario):
    palabra=input('Ingrese la palabra en Ingles a consultar:')
    if palabra in diccionario:
        print('En castellano significa:',diccionario[palabra])
#principal
diccionario=ingresar()
imprimir(diccionario)
consultaPalabra(diccionario)
