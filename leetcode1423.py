from typing import List
class Solution:
    def maxScore2(self, cardPoints: List[int], k: int) -> int:
        if k>=len(cardPoints):
            return sum(cardPoints)
        self.dp = [[0 for _ in range(len(cardPoints))] for _ in range(len(cardPoints))]
        self.ans = float('-inf')
        # self.helper(cardPoints,0,len(cardPoints)-1,k)
        return self.helper(cardPoints,0,len(cardPoints)-1,k)
    
    def helper(self,cardPoints,i,j,k):
        if k==0:
            return self.dp[i][j]
        if self.dp[i][j]!=0:
            return self.dp[i][j]
        res = max(self.helper(cardPoints,i+1,j,k-1)+cardPoints[i],self.helper(cardPoints,i,j-1,k-1)+cardPoints[j])
        self.dp[i][j] = res
        return self.dp[i][j]

        size = len(cardPoints) - k
        minSubArraySum = float('inf')
        j = curr = 0
        
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        minWin = float('inf')
        curWin = 0
        j = 0
        for i,num in enumerate(cardPoints):
            curWin+=num
            if i-j+1>len(cardPoints)-k:
                curWin-=cardPoints[j]
                j+=1
            if i-j+1==len(cardPoints)-k:
                minWin = min(minWin,curWin)
        return sum(cardPoints)-minWin

x = Solution()
l = [1,2,3,5,6,1]
k = 3
ans = x.maxScore(l,k)
print(ans)