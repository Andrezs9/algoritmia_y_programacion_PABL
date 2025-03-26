# ejercicio 6
dividendo = int(input("ingrese dividendo: "))
divisor = int(input("ingrese divisor: "))

contador = 0
while dividendo >= divisor:
    contador = contador + 1 
    dividendo = dividendo - divisor
    
print (f"cociente: {contador}")
print (f"residuo: {dividendo}"