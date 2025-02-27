#Entradas
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
d = float(input("Ingrese el valor de d: "))

#caja negra
if (d == 0):
    print ((a - c)**2)
elif (d > 0):
    print (((a - b)**3) / d)