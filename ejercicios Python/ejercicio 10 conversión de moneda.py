# Entradas
chelines_austriacos = float(input("Ingrese la cantidad de chelines austriacos: "))
# Conversión de chelines a pesetas (1 chelín austriaco = 9568.71 pesetas)
pesetas = chelines_austriacos * (956.871 / 100)
print(chelines_austriacos,"chelines austriacos equivalen a:",pesetas, "pesetas" )

# Conversión de dracmas a pesetas (100 dracmas = 88.607 pesetas)
dracmas_griegos = float(input("Ingrese la cantidad de dracmas griegos: "))
pesetas = dracmas_griegos * (88.607 / 100)
# Conversión de pesetas a francos franceses (1 franco = 20.110 pesetas)
francos = pesetas / 20.110
print("La cantidad de dracmas griegos es: ",francos, "francos franceses")

# Tasa de cambio
tasa_dolares = 122.499
tasa_liras = 9.289
pesetas = float(input("Ingrese la cantidad de pesetas: "))
dolares = pesetas / tasa_dolares
liras = pesetas / tasa_liras
print("Pesetas equivalentes en dólares: ",dolares)
print("Pesetas equivalentes en liras:",liras)
