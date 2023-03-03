# corroborar que todas las palbras de "note" estan en "magazine", las palabras que estan en "note"
# pueden estar repetidas y deben haber la misma cantida o mas en "magazine" imprima "Yes" o "No"

def checkMagazine(magazine, note):
    rta = all(n in magazine for n in note)
    if rta == True:
        print("Yes")
    else: print("No")
    # esto corrobora que las palabras de note esten en magazine, pero no si hay pabaras repetidas

# En este codigo si se corrobora que esten todas las palabras de "note" incluso las repetidas y es mas optimo
from collections import Counter
def checkMagazine2(magazine, note):
    # Write your code here    
    maga = Counter(magazine)
    nta  = Counter(note)
    if all(nta[x] <= maga[x] for x in nta):
        print("Yes") 
    else: print("No") 

magazine = ["two", "times", "three", "is", "not", "four"]
note = ["two", "times", "two", "is", "four"]
checkMagazine2(magazine, note)