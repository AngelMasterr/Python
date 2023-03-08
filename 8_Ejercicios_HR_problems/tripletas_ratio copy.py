# you need to find number of tripets of indices (i,j,k) such that the elements at those indices are in 
# geometric progression for a given common ratio r and i<j<k
"""example:
arr = [1,4,16,64] -- r = 2
there are [1,4,16] and [4,16,64] = 2 tripets with geometric progresion is 4
"""
import math
from collections import Counter

def countTriplets(arr, r):  
    
    list_count = Counter(arr)    
    max_count = max(arr)
    date_prim = list({x for x in arr if x <= max_count//r**2})
    print(date_prim)
    cant_trip = 0
    if r > 1:
        for i in date_prim:
            for ind_1, num_1 in enumerate(arr):
                if num_1 == i:  
                    cant = 0              
                    for ind_2, num_2 in enumerate(arr[ind_1+1:]):
                        if num_2 == i*r:
                            cant += arr[ind_1+ind_2:].count(i*r*r)
                    cant_trip += cant
        print(cant_trip)            
    else:
        combi = 0
        for i in list_count:
            combi += math.comb(list_count[i],3)
        return(combi) 
        
"""with open("Archivos//8_tripletas_prueba3.txt","r") as prueba:
    list_arr = prueba.readline()
    arr = list(map(int, list_arr.strip().split()))
    r = 3
    print(countTriplets(arr, r))"""

arr = [1, 1, 1, 1]
#arr = [1, 3, 9, 9, 27, 27, 81]
r = 1
print(countTriplets(arr, r))

# 13621903916
# 2325652489 
# 2325652489


# 166661666700000
# 166661666700000

#1123 1100 1089
