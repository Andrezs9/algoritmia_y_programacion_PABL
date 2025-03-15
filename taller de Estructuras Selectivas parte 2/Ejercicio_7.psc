Algoritmo Ejercicio_7
	Escribir "numero"
	leer num
	si num <= 1 Entonces
		Escribir "No es primo"
	SiNo
		primo = Verdadero
		Para i = 2 Hasta num - 1 Hacer
			si num % i = 0 Entonces
				primo = Falso
			FinSi
		FinPara
 	FinSi
	si primo Entonces
		Escribir "Es primo"
	SiNo
		Escribir "No es primo"
	FinSi
FinAlgoritmo
