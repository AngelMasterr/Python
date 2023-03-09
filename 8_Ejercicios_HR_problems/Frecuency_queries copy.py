from collections import defaultdict

def freqQuery(queries):    
    dict_date = defaultdict(int)
    result = []
    for i in queries:
        if i[0] == 1:
            dict_date[i[1]] += 1
        elif i[0] == 2:
            if dict_date[i[1]] > 0:
                dict_date[i[1]] -= 1 
        elif i[0] == 3:
            if len(dict_date) != 0 and max(dict_date.values()) >= i[1]:
                result.append(1)
            else:
                result.append(0)
           
    return(result)
    
    
queries = [[3, 4], [2, 1003], [1, 16], [3, 1]]
queries = [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]] 
#print(freqQuery(queries))

with open("Archivos//9_frecuency_queries//frecuency_queries.txt","r") as prueba:
    list_queries = prueba.readlines()
    queries = list(list(map(int, x.split())) for x in list_queries)  
    print(freqQuery(queries))