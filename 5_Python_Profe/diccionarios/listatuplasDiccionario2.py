def ingresar():
    agenda={}
    continua1='s'
    while continua1=='s':
        fecha=input('Ingrese fecha en formato dd/mm/aa:')
        continua2='s'
        lista=[]
        while continua2=='s':
            hora=input('Ingrese hora de la actividad en formato hh:mm')
            actividad=input('Descripción Actividad:')
            lista.append((hora,actividad))
            continua2=input('Desea Ingresar otra actividad para la misma fecha:')
        agenda[fecha]=lista
        continua1=input('Ingresar otra fecha [s/n]:')
    return agenda

def imprimir(agenda):
    print('Lista completa de la agenda')
    for fecha in agenda:
        print('Para la fecha',fecha)
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)

def consultaFecha(agenda):
    fecha=input('Ingrese Fecha a consultar:')
    if fecha in agenda:
        for hora, actividad in agenda[fecha]:
            print(hora,actividad)
    else:
        print('No hay actividad agendada para dicha fecha')

#principal
agenda=ingresar()
imprimir(agenda)
consultaFecha(agenda)
