# Entrada
cantidad = int(input("Ingrese la cantidad en COP: "))

# caja negra
print("Desglose:")
if cantidad >= 100000:
    print("100000 COP:", cantidad // 100000)
    cantidad = cantidad % 100000

if cantidad >= 50000:
    print("50000 COP:", cantidad // 50000)
    cantidad = cantidad % 50000

if cantidad >= 20000:
    print("20000 COP:", cantidad // 20000)
    cantidad = cantidad % 20000

if cantidad >= 10000:
    print("10000 COP:", cantidad // 10000)
    cantidad = cantidad % 10000

if cantidad >= 5000:
    print("5000 COP:", cantidad // 5000)
    cantidad = cantidad % 5000

if cantidad >= 2000:
    print("2000 COP:", cantidad // 2000)
    cantidad = cantidad % 2000

if cantidad >= 1000:
    print("1000 COP:", cantidad // 1000)
    cantidad = cantidad % 1000

if cantidad >= 500:
    print("500 COP:", cantidad // 500)
    cantidad = cantidad % 500

if cantidad >= 200:
    print("200 COP:", cantidad // 200)
    cantidad = cantidad % 200

if cantidad >= 100:
    print("100 COP:", cantidad // 100)
    cantidad = cantidad % 100

if cantidad >= 50:
    print("50 COP:", cantidad // 50)
    cantidad = cantidad % 50
