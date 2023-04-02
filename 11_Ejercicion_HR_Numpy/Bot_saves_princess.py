"""Princess Peach is trapped in one of the four corners of a square grid. You are in the center of the grid and 
can move one step at a time in any of the four directions. Can you rescue the princess?
Input format
The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. This is followed by an NxN 
grid. Each cell is denoted by '-' (ascii value: 45). The bot position is denoted by 'm' and the princess position is
denoted by 'p'."""

def displayPathtoPrincess(n,grid):
#print all the moves here
    m = n // 2
    for p in range(len(grid)):
        if "p" in grid[p]:
            row = p
            col = grid[p].index("p")       
    
    if row-m > 0:
        for i in range(row-m):
            print("DOWN")
    if col-m < 0: 
        for i in range(abs(col-m)):
            print("LEFT")
    if row-m < 0: 
        for i in range(abs(row-m)):
            print("UP")
    if col-m > 0: 
        for i in range(col-m):
            print("RIGHT")    

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)