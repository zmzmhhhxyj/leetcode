from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.dfs(board,0,0)
        return
    def dfs(self,board,i,j):
        while board[i][j]!='.':
            if j == 8:
                if i==8:
                    return True
                i+=1
                j=0
            else:
                j+=1
        for value in range(1,10):
            if self.trueSudoku(board,i,j,str(value)):
                board[i][j] = str(value)
                if self.dfs(board,i,j):
                    return True
        board[i][j]='.'
        return False


    def trueSudoku(self,board,i,j,c):
        for idx in range(9):
            if board[idx][j]==c or board[i][idx]==c:
                return False
        rbox = int(i/3)*3
        cbox = int(j/3)*3
        for a in range(rbox,rbox+3):
            for b in range(cbox,cbox+3):
                if board[a][b]==c:
                    return False
        return True

x = Solution()
a = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
x.solveSudoku(a)
print(a)

    
