# hay varias filas de personas haciendo cola para comprar la boleta del concierto. a cada quein se le entrego un 
# numero que indica su posicion en la fila, pero hay personas que han sobornado para estar adelante,
# encuentre cuantos sobornos se han hecho e imprima esa cantidad y si alguien ha sobornado a mas de dos 
# imprima "Too chaotic" 


q1 = [2, 1, 5, 3, 4]
q2 = [2, 5, 1, 3, 4]
q3 = [5, 1, 2, 3, 7, 8, 6, 4]
q4 = [1, 2, 5, 3, 7, 8, 6, 4]

def minimumBribes(q):
    # Write your code here
    b = 0
    list_q = q.copy()
    list_q.sort()
    for i in range(len(q)):        
        if q[i] - (i+1) >= 3:
            b = "Too chaotic"
            break     
        b += list_q.index(q[i])
        list_q.remove(q[i])      
    print(b)
            
minimumBribes(q4)