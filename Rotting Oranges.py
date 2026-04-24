'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1. '''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        fresh=0
        q=deque()
        r=len(grid)
        c=len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return 0
        cnt=0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            cnt+=1
            size=len(q)
            for _ in range(size):
                x,y=q.popleft()
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if nx<0 or ny<0 or nx>=r or ny>=c or grid[nx][ny]!=1:
                        continue
                    grid[nx][ny]=2
                    q.append((nx,ny))
                    fresh-=1
        return cnt-1 if fresh==0 else -1


        
