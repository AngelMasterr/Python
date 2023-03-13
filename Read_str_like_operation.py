# eval(): allows us to work a string and convert it into an operation
# takes a string as an argument and evaluates it as a Python expression.

x, k = map(int, input().split())    # x=1 y k=4
polynom = input()                   # x**3 + x**2 + x + 1
result = eval(polynom)              # eval(): read str like to a operation
if result == k:
    print("True")
else:
    print("False")
    