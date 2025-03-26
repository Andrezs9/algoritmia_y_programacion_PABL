# ejercicio 7
estudiantes = int(input("ingrese numero de estudiantes: "))

max_altura = 0

for i in range(estudiantes):
    altura = float(input(f"ingrese numero estudiantes {i + 1}: "))
    if altura > max_altura:
        max_altura = altura

print(f"la mayor altura es: {max_altura}")