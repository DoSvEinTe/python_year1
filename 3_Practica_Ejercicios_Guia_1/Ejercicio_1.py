def lista_palabras():
    # Lista vacía
    lista = []
    i = 1
    # Ciclo para acumular palabras con condición
    while i == 1:
        palabra = input("Ingrese alguna palabra: ")
        lista.append(palabra)

        print("SI = 1")
        print("NO = 0")
        
        confirmacion = int(input("¡Quiere continuar?: "))


        if confirmacion == 0:
            i = 0
    return lista

def contador_caracteres(resultado):
    caracteres_5 = []

    for palabra in resultado:
        if len(palabra) > 5:
            caracteres_5.append(palabra)

    return caracteres_5

resultado = lista_palabras()
resultado_2 = contador_caracteres(resultado)

print(f"Las palabras ingresadas en la lista son: {resultado}")
print(f"Las palabras que tienen más de 5 caracteres en la lista son: {resultado_2}")