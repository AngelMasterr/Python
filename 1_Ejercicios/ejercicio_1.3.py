def utopianTree(n):
    # Write your code here
    cont = 1
    for i in range(1, n+1):
        if i%2 == 1:
            cont *= 2
        else:
            cont += 1
    return cont

def angryProfessor(k, a):
    # Write your code here
    cont = 0
    for i in a:
        if i <= 0:
            cont += 1
    if cont >= k:
        return ("NO")
    else:
        return ("YES")