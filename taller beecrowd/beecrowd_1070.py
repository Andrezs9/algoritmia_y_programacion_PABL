numero_x= int(input())

contador = 0
while contador < 6:
    if numero_x % 2 != 0:
        print(numero_x)
        contador += 1
    numero_x += 1