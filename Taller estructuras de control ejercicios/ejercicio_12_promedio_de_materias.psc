Algoritmo ejercicio_12_promedio_de_materias
	//entrada
	Escribir " Ingrese su calificacion del examen final de matematicas: "
	Leer examen_matematicas
	Escribir " Ingrese la nota de la nota 1 de matematicas: "
	Leer nota_1_matematicas
	Escribir " Ingrese la nota de la nota 2 de matematicas: "
	Leer nota_2_matematicas
	Escribir " Ingrese la nota de la nota 3 de matematicas: "
	Leer nota_3_matematicas
	
	Escribir " Ingrese su calificacion del examen final de física: "
	Leer examen_fisica
	Escribir " Ingrese la nota de la nota 1 de fisica: "
	Leer nota_1_fisica
	Escribir " Ingrese la nota de la nota 2 de fisica: "
	Leer nota_2_fisica
	
	Escribir " Ingrese su calificacion del examen final de quimica: "
	Leer examen_quimica
	Escribir " Ingrese la nota de la nota 1 de quimica: "
	Leer nota_1_quimica
	Escribir " Ingrese la nota de la nota 2 de quimica: "
	Leer nota_2_quimica
	Escribir " Ingrese la nota de la nota 3 de quimica: "
	Leer nota_3_quimica
	//caja negra
	promedio_nota_matematicas = (nota_1_matematicas + nota_2_matematicas + nota_3_matematicas) / 3
	porcentaje_nota_matematicas = promedio_nota_matematicas * 0.10
	porcentaje_examen_matematicas = examen_matematicas * 0.90
	nota_final_matematicas = porcentaje_examen_matematicas + porcentaje_nota_matematicas
	
	promedio_nota_fisica = (nota_1_fisica + nota_2_fisica) / 2
	porcentaje_nota_fisica = promedio_nota_fisica * 0.20
	porcentaje_examen_fisica = examen_fisica * 0.80
	nota_final_fisica = porcentaje_examen_fisica + porcentaje_nota_fisica
	
	promedio_nota_quimica = (nota_1_quimica + nota_2_quimica + nota_3_quimica) / 3
	porcentaje_nota_quimica = promedio_nota_quimica * 0.15
	porcentaje_examen_quimica = examen_quimica * 0.85
	nota_final_quimica = porcentaje_examen_quimica + porcentaje_nota_quimica
	
	promedio_general_3_materias = (nota_final_fisica + nota_final_matematicas + nota_final_quimica) / 3
	
	//salida
	Escribir " Su nota final de matematicas es de: ", nota_final_matematicas
	Escribir " Su nota final de fisica es de: ", nota_final_fisica
	Escribir " Su nota final de quimica es de: ", nota_final_quimica
	Escribir " El promedio de las 3 materias es de: ", promedio_general_3_materias
	
	
FinAlgoritmo