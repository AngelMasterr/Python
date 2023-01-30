# Un curos de python dura minimo: 2.5h, en promedio: 4h y maximo: 7h, el curso que estoy tomando dura: 1.5 h
# entonces compara el curso que estoy tomando contra los otros (minimo, promedio y maximo), tener encuenta que
# el curso promedio sin edicion es de 5h y el que estoy tomando sin edición es de: 3.5h, que porcentaje de
# material inservible se elimina en ambos casos
# para terminar, ver 10 h de este curso cuanto seria equivalente en horas en otros curso

# duracion en horas de otros cursos
otros_cursos_min    = 2.5
otros_cursos_prom   = 4  
otros_cursos_max    = 7
curso_actual        = 1.5   # duración del curso que estoy tomando
chupalo = "cacaca"

# porcentaje de diferencia de duracion de los otros cursos vs curso actual
dif_otro_curso_min  = 100 - (curso_actual / otros_cursos_min * 100)
dif_otro_curso_prom = 100 - (curso_actual / otros_cursos_prom * 100)
dif_otro_curso_max  = 100 - (curso_actual / otros_cursos_max * 100)
print("el curos actual dura un",dif_otro_curso_min,"% menos que el curso minimo")
print(dif_otro_curso_prom)
print(dif_otro_curso_max)