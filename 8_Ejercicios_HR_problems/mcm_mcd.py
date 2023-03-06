#a = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [3, 4]
b = [24, 48]

def mcd(a, b):
    """Calcula el máximo común divisor (mcd) de dos números."""
    while b:
        a, b = b, a % b
    return a

def mcm(numbers):
    """Calcula el mínimo común múltiplo (mcm) de una lista de números."""
    if len(numbers) == 1:
        return numbers[0]
    elif len(numbers) == 2:
        return (numbers[0] * numbers[1]) // mcd(numbers[0], numbers[1])
    else:
        return mcm([numbers[0], mcm(numbers[1:])])
    
mcm_a = mcm(a)
print(mcm_a)  # Output: 7886834500
max_a = max(a)
max_b = max(b)
#compl 

minb = max_b//mcm_a
result=[]
for i in range(1, minb+1):
    if all(j%(mcm_a*i)==0 for j in b):
        result.append(mcm_a*i)

print(result)
#return(len(result))