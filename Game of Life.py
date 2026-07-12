''' 
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything. 

Solution - time - O(nxm), space - O(1)
simple iteration with updates according to rules
for constant space, we need some differentiation from old values and new values
replace new 1s with -1 (sum is only required when value was 1 so check absolute value while doing sum)
replace new 0s with 2
'''

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dir = [(-1,0),(0,-1),(1,0),(0,1),(1,1),(-1,-1),(1,-1),(-1,1)]
        n=len(board)
        m=len(board[0])

        """ new 1s [0-->1] = 2
            new 0s [1-->0] = -1 """

        for i in range(n):
            for j in range(m):
                s=0
                for d in dir:
                    ci=d[0]+i
                    cj=d[1]+j
                    if ci<n and cj<m and ci>=0 and cj>=0 and abs(board[ci][cj])==1:
                        s+=1
                # print(s)
                if board[i][j]==1:
                    if s<2 or s>3:
                        board[i][j]=-1
                        # print("dead")
                if board[i][j]==0 and s==3:
                    board[i][j]=2
                    # print("alive")
        for i in range(n):
            for j in range(m):
                if board[i][j]==-1:
                    board[i][j]=0
                elif board[i][j]==2:
                    board[i][j]=1
        
