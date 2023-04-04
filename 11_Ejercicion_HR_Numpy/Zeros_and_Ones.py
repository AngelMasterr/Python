# zeros()
# The zeros tool returns a new array with a given shape and type filled with 0's.
"""
print numpy.zeros((1,2))                    # Default type is float
#Output : [[ 0.  0.]] 
print numpy.zeros((1,2), dtype = numpy.int) # Type changes to int
#Output : [[0 0]] """

# ones()
# The ones tool returns a new array with a given shape and type filled with 1's.
"""
print numpy.ones((1,2))                     # Default type is float
#Output : [[ 1.  1.]] 
print numpy.ones((1,2), dtype = numpy.int)  # Type changes to int
#Output : [[1 1]]   """

import numpy

#arr = list(map(int, input().split()))
arr = [4, 3, 5] 
# 4 = number of matrixs
# 3 = number of rows
# 5 = number of columns
# if the list only have two values, it creat only one matrix
print(numpy.zeros((arr), dtype=int))
print(numpy.ones((arr), dtype=int))
