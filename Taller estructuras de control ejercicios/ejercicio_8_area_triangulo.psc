Algoritmo ejercicio_8_area_triangulo
	//entradas
	escribir "Ingrese la longitud del lado A: "
	leer lado_A
	Escribir "Ingrese la longitud del lado B: "
	leer lado_B
	Escribir "Ingrese la Longitud del lado C: " 
	leer lado_C
	// Caja negra
	S = (lado_A+lado_B+lado_C)/2
	area = Raiz(S * (S - lado_A) * (S - lado_B) * (S - lado_C))
	//salidas
	Escribir "El área del triángulo es: ", area
	
FinAlgoritmo
	