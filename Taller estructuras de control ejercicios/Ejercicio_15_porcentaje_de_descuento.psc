Algoritmo Ejercicio_15_porcentaje_de_descuento
	//entrada
	Escribir " Ingrese valor final pagado por el producto: "
	Leer valor_final_pagado
	Escribir " Ingrese el PVP, precio de venta al publico: "
	Leer precio_venta_publico
	//caja negra
	valor_descuento = precio_venta_publico - valor_final_pagado
	división = valor_descuento / precio_venta_publico
	porcentaje = división * 100
	//salida
	Escribir "El porcentaje de descuento es de: ", porcentaje "%"
	
FinAlgoritmo