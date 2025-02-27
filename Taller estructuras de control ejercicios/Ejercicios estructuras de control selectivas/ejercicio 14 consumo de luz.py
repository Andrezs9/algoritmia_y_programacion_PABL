# entrada
lectura_anterior = input("Ingrese lectura anterior en Kwh: ")
lectura_actual = input("Ingrese lectura actual en Kwh: ")

# caja negra
if lectura_anterior.replace('.', '', 1).isdigit() and lectura_actual.replace('.', '', 1).isdigit():
    lectura_anterior = float(lectura_anterior)
    lectura_actual = float(lectura_actual)

    consumo = lectura_actual - lectura_anterior

    if consumo <= 100:
        monto_pagar = consumo * 4600
    elif consumo <= 300:
        monto_pagar = 100 * 4600 + (consumo - 100) * 80000
    elif consumo <= 500:
        monto_pagar = 100 * 4600 + 200 * 80000 + (consumo - 300) * 100000
    else:
        monto_pagar = 100 * 4600 + 200 * 80000 + 200 * 100000 + (consumo - 500) * 120000

    print(f"El monto que debe pagar por consumo de luz eléctrica es: {monto_pagar:.2f} COP")
else:
    print("Por favor, ingrese valores numéricos válidos para las lecturas.")
