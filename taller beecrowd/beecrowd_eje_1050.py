
diccionario = {61: "brasilia", 71: "salvador", 11: "sao paulo", 21: "rio de janeiro", 32: "Juiz de fora", 19: "Campinas", 27: "Vitoria", 31: "Belo Horizonte"}
# Leer la entrada
ddd = int(input())  # Ingresar el número de DDD

# Buscar la ciudad correspondiente
if ddd in diccionario:
    print(diccionario[ddd])  # Imprime la ciudad correspondiente
else:
    print("DDD nao cadastrado")  # Mensaje si el DDD no está en la tabla
