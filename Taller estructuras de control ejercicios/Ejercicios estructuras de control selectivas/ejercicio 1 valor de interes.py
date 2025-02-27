# entrada
inversion = float(input("Ingrese valor de inversión: "))
interes = float(input("Ingrese tasa de interés anual (%): "))
tiempo = float(input("Ingrese el tiempo de inversión en años: "))

# caja negra 
valor_interes = inversion * (interes / 100)
interes_total = valor_interes * tiempo

if valor_interes > 100000:
    print("Los intereses superan los 100.000")
    valor_final = inversion + interes_total
    print(f"El valor total con intereses es de: {valor_final} COP")
else:
    print("Los intereses no exceden los 100.000")
    valor_final = inversion + interes_total
    print(f"El valor total con intereses sin reinvertir es de: {valor_final} COP")

# Imprimir el interés total generado
print(f"Intereses generados: {interes_total} COP")
print(f"Cantidad final: {valor_final} COP")
    