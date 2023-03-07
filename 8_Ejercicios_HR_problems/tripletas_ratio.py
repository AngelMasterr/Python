# you need to find number of tripets of indices (i,j,k) such that the elements at those indices are in 
# geometric progression for a given common ratio r and i<j<k
"""example:
arr = [1,4,16,64] -- r = 2
there are [1,4,16] and [4,16,64] = 2 tripets with geometric progresion is 4
"""
import math
from collections import Counter

def countTriplets(arr, r):  
    arr = sorted(arr)
    list_count = Counter(arr) 
    max_count = max(list_count)
    if r > 1:
        print(list_count) 
        print(max_count) 
        factor = 0
        for j in list_count: 
            if j*r in list_count and j*r*r in list_count:
                factor += max(list_count[j], list_count[j*r], list_count[j*r*r])
            elif j*r*r > max_count:
                break
        return(factor)        
    else:
        combi = 0
        for i in list_count:
            combi += math.comb(list_count[i],3)
        return(combi)  

with open("Archivos//8_tripletas_prueba2.txt","r") as prueba:
    list_arr = prueba.readline()
    arr = list(map(int, list_arr.strip().split()))
    r = 2
    print(countTriplets(arr, r))


arr = [1, 3, 9, 9, 27, 81]
r = 3
#print(countTriplets(arr, r))

