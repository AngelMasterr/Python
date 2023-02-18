def print_rangoli(size):
    
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    ancho = 4*(size-1)+1
    alto = size-1
    lista_izq = []
    lista_der = []
    # Parte Superior
    for i in range(-alto, 1):
        lista_izq.append(letras[-i])        
        if i > -alto: 
            lista_der.insert(0,letras[-i+1])            
        lista = lista_izq + lista_der 
        rangoli_sup = "-".join(lista)  
        print(rangoli_sup.center(ancho,"-") )
    # Parte Inferior
    lista_izq = []
    lista_der = []
    tamano = len(lista)//2
    for i in range(tamano):
        lista_izq = lista[0:tamano-i]        
        lista_der = lista[tamano+i+2:]                    
        lista_inf = lista_izq + lista_der
        rangoli_inf = "-".join(lista_inf)
        print(rangoli_inf.center(ancho,"-"))
        
print_rangoli(10)