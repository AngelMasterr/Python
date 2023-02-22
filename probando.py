#a = int(1.0)
#b = bool(1)
numbers = [1,2,3,4,5,6,7]
set1 = {"a", "b", "c", "d"}
set2 = {"c", "d", "e", "f"}
#print(set2.union(set1))
#numbers.append(["a", "b"])
#print(numbers)

def f(*x):
    return sum(x)
print(f(5, 3))