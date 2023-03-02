""" Crear una matriz de ceros de m listas y n elementos, Cada operación consiste en agregar un valor a todos 
los elementos de la matriz entre dos índices dados en queries(a, b, k).

ejemplo: segun el array queries: agregue entre el primero y segundo elemento el valor 100, luego entre el 
segundo y quinto elemento agregue otros 100 y por ultimo entre el tercer y cuarto elemento agregue otros 100

n=5  m=3    a b k
queries:    1 2 100         matriz      100 100 0   0   0
            2 5 100         resultante  100 200 100 100 100
            3 4 100                     100 200 200 200 100 """                 

# metodo 1
def arrayManipulation(n, queries):
    # Write your code here
    mat_ceros = []
    list_ceros = [0]*n
    for i in range(len(queries)):        
        for j in range(n):            
            if queries[i][0] <= j+1 and queries[i][1] > j:
                list_ceros[j] +=  queries[i][2]
        mat_ceros.append(list_ceros.copy()) # cree copia de la lista, si no lo hace la lista se modifica siempre en la mat_ceros
    return (max(max(mat_ceros)))   

# metodo 2 mejorado
def arrayManipulation2(n, queries):
    # Write your code here
    list_ceros = [0]*n
    for a,b,k in queries:        
        for j in range(a-1, b):            
            list_ceros[j] +=  k            
    return max(list_ceros)      
  
# metodo 3 mucho mas mejorado
def arrayManipulation3(n, queries):
    # Write your code here
    list_ceros = [0]*n
    for a,b,k in queries:    
        list_ceros[a-1: b] = [x + k for x in list_ceros[a-1: b]]          
    return max(list_ceros)      

# metodo 4, el mejor metodo, pero no lo entiendo del todo  (este lo copie)
# este metodo solo toma el primer valor del rango "a" y lo iguala a "k" y el ultimo+1 "b+1" y lo iguala a -k, no es 
# necesario llenar la listas con cientos de valores k, se entiende que a partir del primero todo es igual y despues 
# del ultimo se resta k, luego se ordena la lista "sorted" y se realiza la acomulacion. (SE AHORRA MUCHA MEMORIA)
from itertools import accumulate, chain
from operator import itemgetter
def arrayManipulation4(n, queries):
    arr = chain.from_iterable(((a, k), (b + 1, -k)) for a, b, k in queries)    
    return max(accumulate(map(itemgetter(1), sorted(arr))))

# metodo 5, igual al 4 pero sin importar itertools y operator
def arrayManipulation5(n, queries):
    # Write your code here
    list_acom = []
    for a,b,k in queries:    
        list_a, list_b = [a, k], [b+1, -k] 
        list_acom.append(list_a) 
        list_acom.append(list_b)
    list_acom = sorted(list_acom) 
    y = 0
    suma_acom = [y := y + x[1] for x in list_acom] 
    return max(suma_acom)
    #return max(list_acom)   



if __name__ == '__main__':
    with open("Archivos//2Darray_ejercicio_5.txt", 'r') as ftpr:
        
        rows = ftpr.readlines()       
        
        n = 4000
        queries = []
        for row in rows:
            list_row = [int(date) for date in row.split(" ")]
            queries.append(list_row)       
        
        result = arrayManipulation4(n, queries)
        print(result)
        

    7542539201
   