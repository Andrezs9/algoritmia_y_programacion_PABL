#Entradas
categoria = int(input("Ingrese la categoría del trabajador (1-5): "))
sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador en COP: "))

if categoria == 1:
    aumento = 0.10
elif categoria == 2:
    aumento = 0.15
elif categoria == 3:
    aumento = 0.20
elif categoria == 4:
    aumento = 0.40
elif categoria == 5:
    aumento = 0.60
else:
    print("La categoría ingresada no es válida. Ingrese un valor entre 1 y 5.")
    
nuevo_sueldo_bruto = sueldo_bruto * (1 + aumento)
print(f"El nuevo sueldo bruto del trabajador es: {nuevo_sueldo_bruto:.2f} COP")
print(f"La categoría del trabajador es: {categoria}")