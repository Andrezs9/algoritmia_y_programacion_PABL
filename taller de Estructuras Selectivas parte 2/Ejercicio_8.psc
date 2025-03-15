Algoritmo Ejercicio_8
	Escribir "Ingrese calificacion"
	Leer Nota1
	si Nota1 = 90 Entonces
		Escribir "A"
	SiNo
		si Nota1 >= 80 y Nota1 < 90 Entonces
			Escribir "B"
		SiNo
			si Nota1 >= 70 y Nota1 < 80 Entonces
				Escribir "c"
			SiNo
				si Nota1 >= 60 y Nota1 < 70 Entonces
					Escribir "D"
				SiNo
					si Nota1<60 Entonces
						Escribir "F"
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
