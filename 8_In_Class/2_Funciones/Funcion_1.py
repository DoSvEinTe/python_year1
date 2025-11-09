#Funcion, programa que calcule el IVA de una compra, siuendo el IVA del 19% sobre el valor total de la compra

def iva(compra):
    compra_iva = compra + compra * 0.19
    return compra_iva

#Ingreso de datos

compra = float(input("Ingrese el valor total de su compra: "))

#Asignacion a una variable

compra_iva = iva(compra)

#Imprimir el resultado

print("El valor de su compra con IVA incluido es de {}".format(compra_iva))
        
        