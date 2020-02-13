from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board,i,j,word,0):
                    return True
        return False

    def helper(self,board,i,j,word,pos):
        if pos == len(word):
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]=='0' or board[i][j]!=word[pos]:
            return False
        tmp = board[i][j]
        board[i][j] = '0'
        if self.helper(board,i-1,j,word,pos+1) or \
            self.helper(board,i+1,j,word,pos+1) or \
                self.helper(board,i,j-1,word,pos+1) or \
                    self.helper(board,i,j+1,word,pos+1):
                    return True
        board[i][j]=tmp
        return False

a = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
x = Solution()
print(x.exist(a,"ABCB"))