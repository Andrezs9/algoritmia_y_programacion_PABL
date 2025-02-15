Algoritmo ejercicio_5_calificacion_final
	//Entrada
	Escribir " Su calificacion final de Computo se compone por: "
	Escribir " 55% de promedio de parciales, 30% de examen final y 15% de trabajo final "
	
	Escribir " Ingrese nota 1: "
	Leer nota1
	Escribir " Ingrese nota 2: "
	Leer nota2
	Escribir " Ingrese nota 3: "
	Leer nota3
	Escribir " Ingrese calificacion del examen final: "
	Leer examen_final
	Escribir " Ingrese calificacion del trabajo final: "
	Leer trabajo_final
	//caja negra
	promedio_notas = (nota1 + nota2 + nota3) / 3
	porcentaje_notas = promedio_notas * 0.55
	porcentaje_examen = examen_final * 0.30
	porcentaje_trabajo = trabajo_final * 0.15
	calificacion_final = porcentaje_examen + porcentaje_notas + porcentaje_trabajo
	//salidas
	Escribir " Su calificacion final de Computo es de: ", calificacion_final
	
FinAlgoritmo