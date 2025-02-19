#Entrada
mujeres = int(input("Número de mujeres: "))
hombres = int(input("Número de hombres: "))

#caja negra
total_estudiantes = mujeres+hombres
porMujeres = (mujeres/total_estudiantes*100)
porHombres = (hombres/total_estudiantes*100)

#salida
print("Porcentaje mujeres: ",porMujeres, "%")
print("porcentaje hombres: ",porHombres, "%")
