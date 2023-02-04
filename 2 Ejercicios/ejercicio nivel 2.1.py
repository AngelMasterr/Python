# Falto el profesor a clases y los estduiantes se organizaron para armar su propia clase, uno de los alumnos va
# hacer de profesor y otro de asistente y van a empezar con
# A) Pedir los datos de los estudiantes que vinieron a clase y ordenar los datos de menor a mayor
# B) El mayor de la clase va ser el profesor y el menor va ser el asistente (quien es el profesor y el asistente)

def cantidad_estudiantes(aaa):    
    estudiantes = []
    for i in range(1, cant_est+1):
        nombre = input(f"Ingrese el nombre del {i} estduiante: ")
        edad = int(input(f"ingrese la edad del {i} estudiante: "))
        compañero = (nombre, edad) # se crea una tupla con eso dos valores
        estudiantes.append(compañero) # se agrega la tupla a la lista vacia       
    # sort: ordena los valores de la lista de forma ascendente (cada elemento de esta lista es una tupla que contiene nombre y edad)
    # key: es un parametro para definir una funcion de clave de ordenamiento
    estudiantes.sort(key = lambda x : x[1]) # lambda: toma una tupla "x" y devuelve su segundo elemento x[1] = "edad"
    
    # Encontrar el asistente, el cual es el estudiante con menor edad
    # la lista "estudiantes" ya esta ordenada de forma ascendente por edad
    asistente = estudiantes[0][0] # [0]: indica la primera tupla y el segundo [0]: indica la primera posicion de la primera tupla osea el "nombre"
    # Encontrar el profesor, el cual es el estudiante con mayor edad
    profesor = estudiantes[-1][0] # [-1]: indica la ultima tupla y el segundo [0]: indica la primera posicion de la ultima tupla osea el "nombre"
    
    # guardamos los valores del asistente y profesor
    return asistente, profesor   

cant_est = int(input("Ingrese la cantidad de estudiante que vinieron: "))

asistente, profesor = cantidad_estudiantes(cant_est)     

print(f"El profesor es {profesor} y el asistente es {asistente}")                            