set_a = set(map(int, input().split()))
n = int(input())
set_n = set()
for i in range(n):
    set_n.update(list(map(int, input().split())))
print(set_a.issuperset(set_n))