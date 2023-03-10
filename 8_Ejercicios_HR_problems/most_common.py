from collections import Counter
# create a list of numbers and find the most repeated number
# the counter method help us to findthe number that occur the most. 

def migratoryBirds(arr):
    # first order the list, if there is more than one number with the same number of repetitions 
    # the counter function is ascending
    arr = sorted(arr)
    birds = Counter(arr)
    
    # most_common(x): this method creates a list with "x" tuples most common, [0][0] accesses 
    # the first tuple and the key, [0][1] accesses the first tuple and the value
    most_com = birds.most_common(1)[0][0]
    print(most_com)

arr = [1, 4, 4, 4, 5, 3]
