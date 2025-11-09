#Funcion, Programa que toma las tres notas de un estudiante y diga la nota final del curso, Tenga en cuenta que la primera y segunda nota vale el 30% de la nota final. La tercera nota vale el 40%
def promedio(nota1, nota2, nota3):
    result1 = nota1 * 0.30
    result2 = nota2 * 0.30
    result3 = nota3 * 0.40

    result_final = (result1 + result2 + result3) / 1

    return result_final

nota1 = int(input("Ingrese su primera nota sin coma: "))
nota2 = int(input("Ingrese su segunda nota sin coma: "))
nota3 = int(input("Ingrese su tercera nota sin coma: "))

va_promedio = promedio(nota1, nota2, nota3)

print("El promedio de las 3 notas es: {}".format(va_promedio))