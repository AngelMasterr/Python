
def activityNotifications(expenditure, d):
    # Write your code here    
    if d % 2 == 0:
        dm1 = int(d/2); dm2 = int(d/2)-1
    else:
        dm1 = dm2 = int((d-1)/2) 
    
    noti = 0
    expend = sorted(expenditure[:d])
    length = len(expenditure)
    
    while len(expend) < length:        
        med = (expend[dm1]+expend[dm2])
        if expenditure[d] >= med:
            noti += 1
            # nearest = max(expend[dm2:], key=lambda y: abs(y - expenditure[d]))
            expend.append(expenditure[d])
        else:
            # nearest = min(expend, key=lambda y: abs(y - expenditure[d]))            
            expend.append(expenditure[d]) 
            
        length -= 1
        a = expenditure[0]
        expend.remove(a)
        expend.sort()
        expenditure.pop(0)
            
    return noti
        
with open("Archivos//8_Fraudulent_Activity//Fraudulent_Activity.txt","r") as prueba: 
    lineas = prueba.readlines()
    linea_1 = list(map(int, lineas[0].split()))
    linea_2 = list(map(int, lineas[1].split()))    
    print(activityNotifications(linea_2 ,linea_1[1]))
    
d = 5
lista = [2, 2, 2, 5, 6, 3, 3, 3, 3, 3, 8, 4, 4, 4, 4, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 6, 6, 6, 8, 8, 4, 5]
print(activityNotifications(lista ,d))
