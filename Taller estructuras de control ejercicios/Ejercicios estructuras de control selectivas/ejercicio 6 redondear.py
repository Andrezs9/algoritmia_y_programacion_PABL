# entrada
entrada = input("Ingrese los números separados por un espacio: ").split()
A = int(entrada[0])
B = int(entrada[1])
C = int(entrada[2])
D = int(entrada[3])

# caja negra
N = A * 1000 + B * 100 + C * 10 + D

if N % 100 >= 50:
    N = (N // 100 + 1) * 100
else:
    N = (N // 100) * 100

# salida
print(N)
