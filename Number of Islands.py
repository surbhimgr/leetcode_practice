''' Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water. 

Solution - Traverse each element of the grid. when u encounter 1, call dfs function to explore its neighbours(when they 1) and change their values inplace to mark them as "visited". Increase counter whenever u encounter a new 1(unvisited before).
Basically we're traversing through each element to the grid, find 1s and mark all the 1s connected to it to mark a complete island.
'''

# Interative (faster)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid,i,j):
            s=[]
            s.append((i,j))
            while len(s)>0:
                a,b=s.pop()
                grid[a][b]="X"
                if a>0 and grid[a-1][b]=="1":
                    s.append((a-1,b))
                if b>0 and grid[a][b-1]=="1":
                    s.append((a,b-1))
                if a<len(grid)-1 and grid[a+1][b]=="1":
                    s.append((a+1,b))
                if b<len(grid[0])-1 and grid[a][b+1]=="1":
                    s.append((a,b+1)) 
        cnt=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    dfs(grid,i,j)
                    cnt+=1
        return cnt

# Recursive

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid,i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return
            if grid[i][j]=="1":
                grid[i][j]="#"
                dfs(grid,i+1,j)
                dfs(grid,i-1,j)
                dfs(grid,i,j+1)
                dfs(grid,i,j-1)
        cnt=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    dfs(grid,i,j)
                    cnt+=1
        return cnt
