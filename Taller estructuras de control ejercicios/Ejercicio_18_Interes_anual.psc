Algoritmo Ejercicio_18_Interes_anual
	// Entrada
	Escribir " Ingrese el valor capital del prestamo: "
	leer capital
	Escribir " ingrese el valor de interes pagado: "
	leer valor_de_interes
	Escribir " ingrese tiempo de prestamo en años: "
	leer tiempo
	// caja negra
	interes = ( valor_de_interes * 100 ) / ( capital * tiempo )
	// salida
	Escribir " porcentaje anual cobrado es de: " interes, "%"
	
FinAlgoritmo
