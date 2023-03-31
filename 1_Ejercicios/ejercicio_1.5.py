"""set_a = set(map(int, input().split()))
n = int(input())
set_n = set()
for i in range(n):
    set_n.update(list(map(int, input().split())))
print(set_a.issuperset(set_n))
"""

def numTilePossibilities(tiles: str) -> int:
        from itertools import permutations
        set_com = set()
        for i in range(len(tiles)):
            set_com.update(list(permutations(tiles,i+1)))
        return(len(set_com))
        
tiles = "AAB"
print(numTilePossibilities(tiles))


def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        flower = []
        a = 1
        for i in range(n):
            for j in range(len(paths)):
                if a in paths[j]:
                    flower.append(a)
                    a += 1
                if a > 4: a = 1
        return(list(set(flower)))

n = 3
paths = [[1,2],[2,3],[3,1]]
print(gardenNoAdj(n, paths))