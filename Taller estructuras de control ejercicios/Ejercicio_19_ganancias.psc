Algoritmo Ejercicio_19_ganancias
	//entradas
	Escribir "Ingrese el numero total de naranjas: "
	leer x
	Escribir "Ingrese el precio por docena: "
	leer u
	Escribir "Ingrese el valor total de ingresos: "
	Leer k
	//caja negra
	costo_total = ( x * u ) / 12
	ganancia_final = k - costo_total
	porcentaje_ganancia = ( ganancia_final / costo_total ) * 100
	//salidas
	Escribir "El porcentaje de su inversión es: ", porcentaje_ganancia "%"
	
FinAlgoritmo