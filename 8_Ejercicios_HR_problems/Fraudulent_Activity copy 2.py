
def activityNotifications(expenditure, d):
    def find(sample, c, d):
        m, n = 0, d-1
        while (n >= m):
            i = (m + n) // 2
            if sample[i] < c:
                m = i + 1
            elif sample[i] > c:
                n = i - 1
            else:
                return i
        n = min(m,n)
        while n < d and sample[n] < c: n += 1
        return n

    notices = 0
    mid, mod = divmod(d, 2)
    sample = sorted(expenditure[:d])
    for start in range(d, len(expenditure)):
        a, b, c = sample[mid-1], sample[mid], expenditure[start]
        limit = b*2 if mod else a+b
        if c >= limit:
            notices += 1
        sample.pop(find(sample, expenditure[start-d], d))
        sample.insert(find(sample, c, d-1), c)
    return notices
        
with open("Archivos//8_Fraudulent_Activity//Fraudulent_Activity.txt","r") as prueba: 
    lineas = prueba.readlines()
    linea_1 = list(map(int, lineas[0].split()))
    linea_2 = list(map(int, lineas[1].split()))    
    print(activityNotifications(linea_2 ,linea_1[1]))
    
d = 5
lista = [2, 2, 2, 5, 6, 3, 3, 3, 3, 3, 8, 4, 4, 4, 4, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 6, 6, 6, 8, 8, 4, 5]
print(activityNotifications(lista ,d))
