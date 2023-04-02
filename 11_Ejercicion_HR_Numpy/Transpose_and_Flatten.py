# Transpose():
# The transpose of a NumPy array is a new array where the rows become columns, and the columns become rows. 
#In other words, it reflects the elements of the array over its main diagonal.
"""
my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print numpy.transpose(my_array)
#Output
[[1 4]
 [2 5]
 [3 6]]"""

# Flatten():
# The flatten method in NumPy returns a one-dimensional version of the input array. This means that all of the 
# elements of the array are put into a single row, with no regard for their original row or column position.
"""
my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print my_array.flatten()
#Output
[1 2 3 4 5 6]"""

import numpy

n, m = map(int, input().split()) # number of rows and columns
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr = numpy.array(arr)
arr_t = numpy.transpose(arr)
print(arr_t)
print(arr.flatten())
    


