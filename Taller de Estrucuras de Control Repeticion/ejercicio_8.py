# ejercicio 8 
total_consumidores = 0
total_mujeres_menores = 0
total_hombres_no_aguardiente = 0
edad_cerveza = 0
total_whisky = 0
total_encuestados = 0

continuar = "si"

while continuar () == "si":
    total_encuestados = total_encuestados + 1
    consume_alcohol= input("¿consume licor? (s/n):")
    if consume_alcohol == "s"
    total_consumidores = total_consumidores + 1 
    
    licor_preferido = int (input("ingrese licor preferido (1-Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro):"))
    edad= int(input("ingrese edad:"))
    sexo input("ingrese sexo (hombre/mujer):")
    if sexo = hombre and licor_preferido != 1 and 20 <= edad <= 25:
        total_hombres_no_aguardiente = total_hombres_no_aguardiente + 1 
    if licor_preferido == 3:
        edad_cerveza = edad_cerveza + 1 
    if licor_preferido == 5:
        total_whisky = total_whisky + 1 
        
input ("desea continar con la encuesta (si/no):")

print(f"Total de mujeres menores de edad: {total_mujeres_menores}")
promedio_edad_cerveza = edad_cerveza / contador_cerveza if contador_cerveza > 0
porcentaje_whisky = (total_whisky / total_encuestados) * 100 if total_encuestados > 0

print(f"Total de personas que consumen licor: {total_consumidores}")
print(f"Total de mujeres menores de edad: {total_mujeres_menores}")
print(f"Total de hombres que no consumen aguardiente y tienen entre 20 y 25 años: {total_hombres_no_aguardiente}")
print(f"Promedio de edad de quienes consumen cerveza: {promedio_edad_cerveza:.2f}")
print(f"Porcentaje de personas que consumen whisky respecto al total encuestado: {porcentaje_whisky:.2f}%")
