# try & except: The statements try and except can be used to handle selected exceptions. A try statement
# may have more than one except clause to specify handlers for different exceptions.

n = int(input())
for i in range(n):
    a, b = input().split()
    
    try:
        print(int(int(a)//int(b)))  # int // int: nothing error, perfect
    except ZeroDivisionError as e:  # int // 0: 
        print("Error Code:",e)      # Error Code: integer division or modulo by zero
    except BaseException as e:      # int // "$": 
        print("Error Code:",e)      # Error Code: invalid literal for int() with base 10: '$' 
    
