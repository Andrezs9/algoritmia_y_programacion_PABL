a = int(input())

for _ in range(a):
    entrada = input().split()
    heroe = entrada[0]
    fuerza = int(entrada[1])
    
    if heroe == "Thor":
        print("Y")
    else:
        print("N")