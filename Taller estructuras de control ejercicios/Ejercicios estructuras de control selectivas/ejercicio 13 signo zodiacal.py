# Entrada
fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
dia, mes, año = map(int, fecha_nacimiento.split('/'))


from datetime import datetime

# Caja negra
def obtener_signo_zodiacal(dia, mes):
    if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
        print("Capricornio")
    elif (mes == 1 and dia >= 21) or (mes == 2 and dia <= 19):
        print("Acuario")
    elif (mes == 2 and dia >= 20) or (mes == 3 and dia <= 19):
        print("Piscis")
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
        print("Aries")
    elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 21):
        print("Tauro")
    elif (mes == 5 and dia >= 22) or (mes == 6 and dia <= 21):
        print("Géminis")
    elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 22):
        print("Cáncer")
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 23):
        print("Leo")
    elif (mes == 8 and dia >= 24) or (mes == 9 and dia <= 22):
        print("Virgo")
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        print("Libra")
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        print("Escorpión")
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        print("Sagitario")

print("Su signo zodiacal es:", end=" ")
obtener_signo_zodiacal(dia, mes)

fecha_actual = datetime.now()
fecha_nacimiento = datetime(año, mes, dia)
edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

# Salida
print(f"Su edad es: {edad} años")
