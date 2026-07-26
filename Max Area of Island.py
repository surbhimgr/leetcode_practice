''' You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0. '''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirc=[(1,0),(0,1),(-1,0),(0,-1)]
        n=len(grid)
        m=len(grid[0])
        def dfs(ci,cj):
            grid[ci][cj]=2
            area=1
            for d in dirc:
                ni=d[0]+ci
                nj=d[1]+cj
                if ni>=0 and nj>=0 and ni<n and nj<m and grid[ni][nj]==1:
                    area+=dfs(ni,nj)
            return area

        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:                   
                    ans=max(ans,dfs(i,j))
        return ans
