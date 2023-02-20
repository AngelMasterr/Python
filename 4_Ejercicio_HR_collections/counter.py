# The first line contains X, the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains N, the number of customers.
# The next N lines contain the space separated values of the (shoe size) desired by the customer and x, the price of the shoe.
""" Sample Input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50 """

from collections import Counter

shoes = int(input())
shoe_size = Counter(map(int, input().split()))
customers = int(input())
profit = 0
for i in range(customers):    
    size, price = map(int, input().split())
    if size in shoe_size and shoe_size[size] > 0:
         profit += price
         shoe_size[size] -= 1
    
print(profit)
