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
  

if __name__ == '__main__':
    with open("Archivos//2Darray_ejercicio_5.txt", 'r') as ftpr:
        
        rows = ftpr.readlines()       
        
        n = 4000
        queries = []
        for row in rows:
            list_row = [int(date) for date in row.split(" ")]
            queries.append(list_row)       
        
        result = arrayManipulation3(n, queries)
        print(result)
        

    7542539201
    7542539201