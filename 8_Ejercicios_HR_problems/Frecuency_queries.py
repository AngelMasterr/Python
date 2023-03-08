from collections import Counter

def freqQuery(queries):    
    arr = []; result = []
    for i in queries:
        if i[0] == 1:
            arr.append(i[1])
        elif i[0] == 2 and i[1] in arr:
            arr.remove(i[1])
        elif i[0] == 3:
            comp = Counter(arr)
            sorted_comp = sorted(comp.values())
            if sorted_comp != []:
                if sorted_comp[-1] >= i[1]:
                    result.append(1)
                else:
                    result.append(0)
            else:
                result.append(0)
    return(result)
    
    
#queries = [[1, 4], [2, 1003], [1, 16], [3, 1]]
queries = [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]] 
#freqQuery(queries)

with open("Archivos//9_frecuency_queries//frecuency_queries.txt","r") as prueba:
    list_queries = prueba.readlines()
    queries = list(list(map(int, x.split())) for x in list_queries)  
    print(freqQuery(queries))