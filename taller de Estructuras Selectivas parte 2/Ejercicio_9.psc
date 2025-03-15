Algoritmo Ejercicio_9
	Escribir "ingrese numero"
	Leer num
	l = Longitud(num)
	j = l
	c = 0 
	para i = 1 Hasta l
		si Subcadena(num,i,i) = Subcadena(num,j,j)
			c=c+1
		FinSi
		j=j-1
	FinPara
	
	si c=l Entonces
		Escribir "es palindromo"
	SiNo
		Escribir "no es palindromo"
		
		
	FinSi
FinAlgoritmo
