
numeros = []

for i in range(6):
    numeros.append(float(input()))

positivos = [num for num in numeros if num > 0]

cantidad_positivos = len(positivos)

promedio = sum(positivos) / cantidad_positivos if cantidad_positivos > 0 else 0

print(cantidad_positivos)
print(f"{promedio:.1f}")