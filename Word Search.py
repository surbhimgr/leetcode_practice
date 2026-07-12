''' 
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once. 

Solution - DFS + backtraking + marking visited nodes
if current node matches with first word of target, we mark it visited and check neighbouring nodes with remaining letters of target
else we backtrack
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        ans=False
        dir=[(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(dfsi : int, dfsj : int , rem : List[int], vis : set):
            # print(dfsi,dfsj,rem)
            # print("outside true ans")
            # print(len(rem))
            nonlocal ans  --> so that we can modify value of ans which outside of current function scope
            if ans:
                return
            if not rem:
                ans= True
                # print("inside true ans")
                return
            for d in dir:
                ci=d[0]+dfsi
                cj=d[1]+dfsj
                # print(ci,cj,board[ci][cj],rem[0])
                if ci>=0 and cj>=0 and ci<n and cj<m and (ci,cj) not in vis and board[ci][cj]==rem[0]:
                    vis.add((ci,cj))
                    dfs(ci,cj,rem[1:],vis)
                    vis.remove((ci,cj))
            return
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    dfs(i,j,word[1:],{(i,j)})
        return ans

                    
