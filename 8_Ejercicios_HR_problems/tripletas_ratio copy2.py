# you need to find number of tripets of indices (i,j,k) such that the elements at those indices are in 
# geometric progression for a given common ratio r and i<j<k
"""example:
arr = [1,4,16,64] -- r = 2
there are [1,4,16] and [4,16,64] = 2 tripets with geometric progresion is 4
"""
import math
from collections import Counter
from itertools import product

def countTriplets(arr, r):  
    
    list_count = Counter(arr)    
    max_count = max(arr)
    date_prim = list({x for x in arr if x <= max_count//r**2})
    print(date_prim)
    
    total = 0
    if r > 1:
        for i in date_prim:            
            indice =    [ind for ind, x in enumerate(arr) if x == i]  
            indice_r =  [ind for ind, x in enumerate(arr) if x == i*r] 
            indice_r2 = [ind for ind, x in enumerate(arr) if x == i*r*r]            
            prod = list(product(indice, indice_r, indice_r2))
            selec_sort = [x for x in prod if x[0]<x[1] and x[1]<x[2]]
            total += len(selec_sort)
        
        print(total)      
    else:
        combi = 0
        for i in list_count:
            combi += math.comb(list_count[i],3)
        return(combi) 
        
with open("Archivos//8_tripletas_ratio//8_tripletas_prueba3.txt","r") as prueba:
    list_arr = prueba.readline()
    arr = list(map(int, list_arr.strip().split()))
    r = 3
    print(countTriplets(arr, r))

#arr = [1, 1, 1, 1]
arr = [1, 3, 9, 9, 27, 81]
r = 3
#print(countTriplets(arr, r))

# 13621903916
# 2325652489 
# 2325652489


# 166661666700000
# 166661666700000

#1123 1100 1089
