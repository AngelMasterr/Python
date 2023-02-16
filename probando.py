if __name__ == '__main__':
    lista = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        datos = (name, score)
        lista.append(datos)
    
    lista.sort(key = lambda x: x[1])  
    
    n = 0; 
    # comprobar si el valor mas bajo esta repetido
    while lista[n][1] == lista[n+1][1]:   n += 1 
    m = n + 1 
    tamaño = len(lista)-1
    # comprobar si el segundo valor mas bajo esta repetido
    if m < tamaño:
        while lista[m][1] == lista[m+1][1]:   
            if m < tamaño: m += 1
            else: break 
    
    names = []
    for i in range(n+1, m+1):
        names.append(lista[i][0])
    names.sort(key = lambda x: x[0])
    for nu in range(len(names)): 
        print(names[nu])   