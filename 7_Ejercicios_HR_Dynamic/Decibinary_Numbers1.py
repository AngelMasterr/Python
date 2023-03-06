def decibinary(n):
    import math
    from itertools import product    
    # create the equation and length according to the integer n
    long = int(math.log(n,2)+1)
    list_x = []
    for i in range(long):
        a = 2**i
        list_x.append(a)    # if n in (4:7)  - list_x=[4 2 1]
    list_x.reverse()        # if n in (8:15) - list_x=[8 4 2 1]
    # print(list_x)
    # create a dictionary with all the ranks of each element according to the length of the equation log(n,2)
    variables = {}
    for i in range(len(list_x)):
        key_var =  "range_"+str(i+1)
        value_var = list(range(0, int(n/list_x[i])+1))
        variables[key_var] = value_var
    #print(variables.items())
    list_prod = product(*variables.values())
    prod_values = list(list_prod)
    # print(prod_values)
    # create the variables according to the number of lists in the dict
    charact = []
    for pa in range(len(list_x)):
        charact.append(f"{chr(97+pa)}") 
    characters = ",".join(charact)
    #print(characters)
      
    if len(list_x) == 2: combinations = [(b, a) for b, a in prod_values if 2*b + a == n]
    if len(list_x) == 3: combinations = [(c, b, a) for c, b, a in prod_values if 4*c + 2*b + a == n]
    if len(list_x) == 4: combinations = [(d, c, b, a) for d, c, b, a in prod_values if 8*d + 4*c + 2*b + a == n]
    if len(list_x) == 5: combinations = [(e, d, c, b, a) for e, d, c, b, a in prod_values if 16*e + 8*d + 4*c + 2*b + a == n]
    if len(list_x) == 6: combinations = [(f, e, d, c, b, a) for f, e, d, c, b, a in prod_values if 32*f + 16*e + 8*d + 4*c + 2*b + a == n]
    if len(list_x) == 7: combinations = [(g, f, e, d, c, b, a) for g, f, e, d, c, b, a in prod_values if 64*g + 32*f + 16*e + 8*d + 4*c + 2*b + a == n]
    
    numeros = [int(''.join(map(str, t)).replace(',', '')) for t in combinations]
    #print(numeros) 
    return numeros   

n=1000
list_total = [0,1]
m = 2  
while len(list_total) < n:     
    list_total += decibinary(m)
    m += 1
list_total = list_total
print(list_total)
print(list_total[n-1])