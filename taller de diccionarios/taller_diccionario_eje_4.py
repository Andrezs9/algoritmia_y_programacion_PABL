estudiantes = {
    "1": {
        "nombre": "Lorea",
        "nota": 8
    },
    "2": {
        "nombre": "Markel",
        "nota": 4.2
    },
    "3": {
        "nombre": "Julen",
        "nota": 6.5
    }
}
contador = len(estudiantes) + 1
while contador <= 10:
    nombre = input(f"Nombre del estudiante {contador}: ")
    if nombre == "":
        break

    nota = float(input("Nota:"))
    estudiantes[str(contador)] = {"nombre": nombre, "nota": nota}
    contador += 1

aprobados = []
suspendidos = []
suma = 0

for estu in estudiantes.values():
    suma += estu["nota"]
    if estu["nota"] >= 5:
        aprobados.append(estu["nombre"])
    else:
        suspendidos.append(estu["nombre"])

media = suma / len(estudiantes)

print("Aprobados:", aprobados)
print("Suspendidos:", suspendidos)
print(f"Nota media: {media:.2f}")
