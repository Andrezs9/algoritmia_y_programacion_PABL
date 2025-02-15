Algoritmo ejercicio_6_porcentaje_hombres_y_mujeres
	//Entradas
	Escribir " numero de mujeres: "
	Leer mujeres
	Escribir " numero de hombres: "
	Leer hombres
	//caja negra
	total_estudiantes <- mujeres + hombres
	porMujeres <- (mujeres / total_estudiantes * 100)
	porHombres <- (hombres / total_estudiantes * 100)
	//salidas
	Escribir " Porcentaje Hombres ", porHombres "%"
	Escribir " Porcentaje Mujeres ", porMujeres "%"
	
	
FinAlgoritmo