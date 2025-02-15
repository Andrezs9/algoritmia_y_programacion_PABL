Algoritmo ejercicio_10_cambio_de_divisas
	// entradas
	Escribir "Ingrese la cantidad de chelines austriacos: "
	Leer chelines_austriacos
	//conversion 1 chelines_austriacos equivalen a 9568.71 pesetas
	pesetas = chelines_austriacos * (956.871 / 100)
	Escribir chelines_austriacos " chelines austriacos equivalen a: ", pesetas, " pesetas "
	
	//conversion de dracmas a pesetas 100 dracmas = 88.607 pesetas
	escribir "Ingrese la cantidad de dracmas griegos: "
	Leer dracmas_griegos
	pesetas = dracmas_griegos * (88.607 / 100)
	// conversion de pesetas a francos franceses 1 franco = 20.110 pesetas 
	francos = pesetas / 20.110
	escribir " la cantidad de dracmas_griegos es: ", francos
	
	// tasa de cambio 
	tasa_dolares = 122.499
	tasa_liras = 9.289
	Escribir " ingrese la cantidad de pesetas: "
	leer pesetas
	dolares = pesetas / tasa_dolares
	liras = pesetas / tasa_liras
	escribir "pesetas equivalente en dolares: " , dolares
	Escribir "pesetas equivalente en liras: " , liras
	
	
	
	
FinAlgoritmo
