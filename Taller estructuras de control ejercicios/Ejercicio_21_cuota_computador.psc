Algoritmo Ejercicio_21_cuota_computador
	// Entradas
	
    Escribir "Ingrese el precio del computador a contado: "
    Leer precio
    Escribir "Ingrese el valor de cada cuota: "
    Leer cuotas
	
    // Caja negra
    total_cuotas = cuotas * 12
    interes = total_cuotas - precio
    porcentaje_interes = ( interes / precio ) * 100
    // Salidas
    Escribir "El porcentaje del interes es: ", porcentaje_interes, "%"
	
FinAlgoritmo