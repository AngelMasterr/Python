def utopianTree(n):
    # Write your code here
    cont = 1
    for i in range(1, n+1):
        if i%2 == 1:
            cont *= 2
        else:
            cont += 1
    return cont
