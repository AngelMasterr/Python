# segun la lista de enteros dada, la cual contiene los numero de 1 hasta n, ordenelos de forma ascendere y 
# calcule la cantidad de intercambios que se necesitaron para ordenar la lista

# Primer metodo
def minimumSwaps(arr):
    movs = 0
    for i in range(len(arr)):
        if not arr[i] == i+1:
            arr[arr.index(i+1)] = arr[i]
            arr[i] = i+1
            movs += 1
    return movs

arr = [1, 2, 7, 4, 5, 6, 3]
arr1 = [4, 3, 1, 2]

# Seguno metodo
def minimumSwaps(arr):
    movs = 0
    for i in range(len(arr)):
        while i+1 != arr[i]:
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
            movs += 1        
    return movs

minimumSwaps2(arr1)