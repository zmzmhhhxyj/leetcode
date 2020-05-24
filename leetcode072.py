class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        dp = [[0]*(len2+1) for _ in range(len1+1)]

        for i in range(len1+1):
            dp[i][0] = i
        for j in range(len2+1):
            dp[0][j] = j
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
        return dp[-1][-1]

    def minDistance2(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word2) if word2 else len(word1)
        dp = [[1 for _ in range(len(word1))] for _ in range(len(word2))]
        if word1[0]==word2[0]:
            dp[0][0] = 0
        repe = False
        for i in range(1,len(word1)):
            if word2[0]==word1[i] and repe==False:
                dp[0][i]=dp[0][i-1]
                repe = True
            else:
                dp[0][i]=dp[0][i-1]+1
        repe = False
        for i in range(1,len(word2)):
            if word1[0]==word2[i] and repe == False:
                dp[i][0] = dp[i-1][0]
                repe = True
            else:
                dp[i][0] = dp[i-1][0]+1
        for i in range(1,len(word2)):
            for j in range(1,len(word1)):
                if word2[i]==word1[j]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[-1][-1]

# word1 = "intention", word2 = "execution"
x = Solution()
# res = x.minDistance("intention","execution")
res = x.minDistance("pneumonoultramicroscopicsilicovolcanoconiosis","ultramicroscopically")
print(res)