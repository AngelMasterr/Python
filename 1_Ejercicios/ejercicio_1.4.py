from collections import Counter
k = int(input())
rooms = list(map(int, input().split()))
room_cap = [x for x,y in (Counter(rooms)).items() if y == 1]
print(*room_cap)