# Concatenate
# Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:
"""
array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])
print numpy.concatenate((array_1, array_2, array_3)) 
#Output
[1 2 3 4 5 6 7 8 9]"""

# If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are
# concatenated. By default, it is along the first dimension.
"""
array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])
print numpy.concatenate((array_1, array_2), axis = 1)   
#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]"""
 
import numpy

n, m, p = map(int, input().split())
np = []; mp = []
for i in range(n):
    np.append(list(map(int, input().split())))
for j in range(m):
    mp.append(list(map(int, input().split())))
np = numpy.array(np)
mp = numpy.array(mp)
#print(np, mp)
print(numpy.concatenate((np, mp), axis=0))