Algoritmo Ejercicio_14_monto_a_pagar_por_luz
	//Entradas
	Escribir " Ingrese la lectura anterior: "
	Leer lectura_anterior
	escribir "Infrese la lectura_actual: "
	Leer lectura_actual
	Escribir " ingrese el costo por kilovatio: "
	leer costo_por_kilovatio
	// caja negra
	consumo = lectura_actual - lectura_anterior
	montototal = consumo * costo_por_kilovatio
	// salidas
	Escribir "el monto total a pagar es de: " , montototal
	
FinAlgoritmo
