from collections import Counter
k = int(input())
rooms = list(map(int, input().split()))
room_cap = [x for x,y in (Counter(rooms)).items() if y == 1]
print(*room_cap)

t = int(input())
for i in range(t):
    a = int(input())
    set_a = set(map(int, input().split()))
    b = int(input())
    set_b = set(map(int, input().split()))
    print(set_a.issubset(set_b))
     