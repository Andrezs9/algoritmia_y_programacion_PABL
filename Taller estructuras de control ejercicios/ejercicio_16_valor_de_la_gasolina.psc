Algoritmo ejercicio_16_valor_de_la_gasolina
	// Entrada
	Escribir " Ingrese la cantidad de galones suministrados: "
	leer cantidad_de_galones
	// caja negra
	galones_a_litros = 3.785
	precio_por_litro = 50000
	litros = cantidad_de_galones * galones_a_litros
	monto_total = litros * precio_por_litro
	// salida
	Escribir " El monto total a pagar es de: " , monto_total
	
FinAlgoritmo
