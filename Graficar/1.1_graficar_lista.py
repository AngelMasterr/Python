# Crear un grafico con las notas de 10 estudiantes

import matplotlib.pyplot as plt

x = list(range (10))
y = [3, 7, 5, 6, 8 , 4, 7, 10, 1, 9]

plt.plot(x, y, marker = 'o')  # "marker: pone un caracter en cada quiebre de la linea"
plt.title('Grafico de notas de los estudiantes')
plt.xlabel('Codigo del estudiante')
plt.ylabel('Notas del estudiante')
plt.show()