imm=460000 # ingreso minimo mensual al 1 de abril 2024
movilizacion=50000
colacion=50000
def datosTrabajador(rut,nombre,dt,sb,he,cf):
    print("*******************************************************************")
    print("\t\tLIQUIDACION DE SUELDO POR PANTALLA")
    print("*******************************************************************")
    print("****************** DATOS DEL TRABAJADOR****************************")
    print("Rut\t\t\t:",rut)	
    print("Nombre\t\t\t:",nombre)
    print("Días Trabajados\t\t:",dt)
    print("Sueldo Base\t\t:",sb)
    print("Numero Horas Extras\t:",he)
    print("Cargas Familiares\t:",cf)
    print("****************************IMPONIBLE******************************")
    print("Valor días trabajados\t:",calculodiastrabajados(dt,sb))
    print("Valor gratificación\t:",gratificacion())	
    print("Valor horas extras\t:",Horasextras(he,sb))
    print("Total Suma de Imponibles:",sumaImponible(dt,sb,he))
    print("****************************NO IMPONIBLE****************************")
    print("Valor Movilización\t:",movilizacion)
    print("Valor colación\t:	",colacion)
    print("Valor Carga Familiar\t:",cargafamiliar(cf,sumaImponible(dt,sb,he)))
    print("Total Suma de No Imponibles\t:",sumNoImponible(cf,sumaImponible(dt,sb,he)))
    print("*************************** DESCUENTOS ****************************")
    print("Valor AFP 12,75% \t:",afp(sumaImponible(dt,sb,he)))
    print("Valor Fonasa 7% \t\t:",fonasa(sumaImponible(dt,sb,he)))
    print("Total Suma Descuentos\t:",sumaDescuentos(sumaImponible(dt,sb,he)))
    print("********************* TOTAL A PAGAR ********************************")
    print("Valor liquido a pagar\t:",totalPagar(dt,sb,he,cf,sumaImponible(dt,sb,he)))
    print("*********************************************************************") 



def calculodiastrabajados(dt,sb):
    return round((sb/30)*dt)

def gratificacion(): 
    return round((imm*4.75)/12)

def Horasextras(he,sb):
    return round(sb*0.007777*he)

def sumaImponible(dt,sb,he):
    return round(calculodiastrabajados(dt,sb)+gratificacion()+Horasextras(he,sb))

def afp(imponible):
    return round(imponible*0.1275)

def fonasa(imponible):
    return round(imponible*0.07)

def sumaDescuentos(imponible):
    return round(afp(imponible)+fonasa(imponible))

def cargafamiliar(cf, imponible):
    #actualizado hasta 31-06-2023
    tramo=0
    if  imponible<=539328:
        tramo= cf*20328
    else:
        if imponible<=787746:
            tramo= cf*12475
        else:
            if imponible<=1228614:
                tramo= cf*3942
            else:
                tramo= 0
    return tramo

def sumNoImponible(cf,imponible):
    return movilizacion+colacion+cargafamiliar(cf,imponible)

def totalPagar(dt,sb,he,cf,imponible):
    return sumaImponible(dt,sb,he)+sumNoImponible(cf,imponible)-sumaDescuentos(imponible)