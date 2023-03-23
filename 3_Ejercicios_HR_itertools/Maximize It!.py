from itertools import product
k, m = map(int, input().split())
list_K = []
for i in range(k):   
    list_K.append(list(set(map(lambda x: int(x)**2, input().split()))))
#print(list_K)
prod_k = list(sum(x)%m for x in product(*list_K))
print(max(prod_k))
"""
k=3, m=1000
n=2, list_n=5 4
n=3, list_n=7 8 9 
n=5, list_n=5 7 8 9 10 """