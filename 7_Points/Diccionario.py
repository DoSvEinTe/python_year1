# Solicitar los datos del trabajador

rut = input("Ingrese su rut: ")
nombre = input("Ingrese su nombre: ")
dt = int(input("Ingrese el total de dias trabajados: "))
sb = int(input("Ingrese su sueldo base: "))
he = float(input("Ingrese sus horas extras: "))
cf = int(input("Ingrese cuantas cargas familiares tiene: "))

# Crear el diccionario con los datos del trabajador

trabajador = {
    rut: (nombre, dt, sb, he, cf)
}

# Variables constantes
movilizacion = 50000
colacion = 50000
imm = 165000

# Suma no imponibles
suma_no_imponibles = movilizacion + colacion

# Definir las funciones

def calculo_dias_trabajados(dt, sb):
    valor_dias_trabajados = (sb / 30) * dt
    return valor_dias_trabajados

def horas_extras(he, sb):
    valor_horas_extras = (sb * 0.007777 * he)
    return valor_horas_extras

def afp(suma_imponibles):
    valor_afp = suma_imponibles * 0.1275
    return valor_afp

def fonasa(suma_imponibles):
    valor_fonasa = (suma_imponibles * 0.07)
    return valor_fonasa

def total_descuentos(valor_afp, valor_fonasa):
    total = valor_afp + valor_fonasa
    return total

# Suma de Imponibles

calc_dias = calculo_dias_trabajados(dt, sb)
calc_horas_ex = horas_extras(he, sb)
suma_imponibles = calc_dias + calc_horas_ex

# Suma haberes

suma_haberes = suma_no_imponibles + suma_imponibles

# Cálculo de descuentos

valor_afp = afp(suma_imponibles)
valor_fonasa = fonasa(suma_imponibles)
total_desc = total_descuentos(valor_afp, valor_fonasa)

# Cálculo del valor líquido a pagar

valor_liquido_a_pagar = suma_haberes - total_desc

# Definir la función para mostrar los datos del trabajador

def test_liquidacion(trabajador):
    print("****************** DATOS DEL TRABAJADOR ****************************\n")
    for rut, datos in trabajador.items():
        nombre, dt, sb, he, cf = datos
        print(f"Rut:                                                     {rut}")
        print(f"Nombre:                                                  {nombre}")
        print(f"Días trabajados:                                         {dt}")
        print(f"Sueldo base:                                             {sb}")
        print(f"Horas extras:                                            {he}")
        print(f"Cargas familiares:                                       {cf}")
    print("\n**************************** IMPONIBLE ****************************\n")
    print(f"Valor días trabajados:          {calculo_dias_trabajados(dt, sb)}")
    print(f"Valor horas extras:                        {horas_extras(he, sb)}")
    print(f"Total suma de Imponibles:                       {suma_imponibles}")
    print("\n**************************** NO IMPONIBLE *************************\n")
    print(f"Valor movilización:                                {movilizacion}")
    print(f"Valor colación:                                        {colacion}")
    print(f"Valor suma de no imponibles:                 {suma_no_imponibles}")
    print("\n*************************** SUMA HABERES *************************\n")
    print(f"Total haberes:                                     {suma_haberes}")
    print("\n*************************** DESCUENTOS ***************************\n")
    print(f"Valor AFP:                                            {valor_afp}")
    print(f"Valor Fonasa:                                      {valor_fonasa}")
    print("")
    print(f"Total suma descuentos:                               {total_desc}")
    print("\n********************* TOTAL A PAGAR *******************************\n")
    print("")
    print(f"Valor líquido a pagar:                    {valor_liquido_a_pagar}")

# Llamar a la función para mostrar los datos del trabajador

test_liquidacion(trabajador)

#Integrantes = Jonathan Gallardo
#              Christofer Paredes
#              Benjamin Velazquez

