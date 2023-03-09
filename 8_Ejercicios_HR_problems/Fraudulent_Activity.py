
def activityNotifications(expenditure, d):
    # Write your code here    
    if d % 2 == 0:
        dm1 = int(d/2); dm2 = int(d/2)-1
    else:
        dm1 = dm2 = int((d-1)/2) 
    
    noti = 0
    for i in range(d, len(expenditure)):
        if d == len(expenditure): break
        expend = sorted(expenditure[(i-d):i])
        #print(expend)
        med = (expend[dm1]+expend[dm2])/2
        #print(expenditure[i])
        
        if expenditure[i] >= 2*med:
            noti += 1
    return noti
        
with open("Archivos//8_Fraudulent_Activity//Fraudulent_Activity.txt","r") as prueba: 
    lineas = prueba.readlines()
    linea_1 = list(map(int, lineas[0].split()))
    linea_2 = list(map(int, lineas[1].split()))
    
    activityNotifications(linea_2 ,linea_1[1])