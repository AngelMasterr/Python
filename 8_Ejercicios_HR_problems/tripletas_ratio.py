# you need to find number of tripets of indices (i,j,k) such that the elements at those indices are in 
# geometric progression for a given common ratio r and i<j<k
"""example:
arr = [1,4,16,64] -- r = 2
there are [1,4,16] and [4,16,64] = 2 tripets with geometric progresion is 4
"""
import math
from itertools import combinations
from collections import Counter

def countTriplets(arr, r):  
    list_count = Counter(arr) 
    print(list_count)   
    if len(list_count) >= 3:
        list_com = list(combinations(list_count,3))    
        triple = []          
        for i in list_com:
            if i[2]/i[1] == r and i[1]/i[0] ==r:
                triple.append(i) 
    else:
        combi = 0
        for i in list_count:
            combi += math.comb(list_count[i],3)
        return(combi)
                       
    value_max = 0
    for i in triple:
        value_max += max(list_count[x] for x in i)        
    print(triple)
    return(value_max)

with open("Archivos//8_tripletas_prueba4.txt","r") as prueba:
    list_arr = prueba.readline()
    arr = list(map(int, list_arr.strip().split()))
    r = 1
    print(countTriplets(arr, r))

arr = [1, 3, 9, 9, 27, 81]
r = 3
#print(countTriplets(arr, r))

# 166661666700000 
# 166661666700000