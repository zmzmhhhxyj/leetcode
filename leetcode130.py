import queue
from typing import List
import collections
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = collections.deque([])
        if len(board)<=2:
            return
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0,len(board)-1] or c in [0,len(board[0])-1]) and board[r][c]=='O':
                    q.append((r,c))
        
        while q:
            r,c = q.pop()
            if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c]=='O':
                board[r][c] = "N"
                q.append((r-1,c))
                q.append((r+1,c))
                q.append((r,c-1))
                q.append((r,c+1))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=="O":
                    board[r][c]="X"
                if board[r][c]=="N":
                    board[r][c]="O"

x = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
x.solve(board)
print(board)

