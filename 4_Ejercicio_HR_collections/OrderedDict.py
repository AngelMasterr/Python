n = int(input()) # number of items
name_price = {}
for i in range(n):
    date = input().split() # name item, price item
    key = " ".join(date[0:-1])
    name_price[key] = int(date[-1])
    
print(name_price)