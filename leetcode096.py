class Solution:

    def numTrees(self, n: int) -> int:
        return self.countNum(n,[-1]*(n+1))
    def countNum(self,n,cache):
        if n == 0 :
            return 1
        if n == 1 :
            return 1
        if cache[n] != -1:
            return cache[n]
        
        res = 0
        for i in range(n):
            left = self.countNum(i,cache)
            right = self.countNum(n-i-1,cache)
            res += left*right
        cache[n] = res
        return res

    """
    def countTrees(n, cache):
        if n == 0:
            return 1
        if n == 1:
            return 1

        if cache[n] != -1: # -1 means we don't know countTrees(n) yet.
            return cache[n]

        Result = 0
        for i in range(n):
            LeftTrees =Solution.countTrees(i, cache)
            RightTrees = Solution.countTrees(n - i - 1, cache)
            Result += LeftTrees * RightTrees
        cache[n] = Result
        return Result
    """

x=Solution()
cache = [-1]*4
a=x.numTrees(3)
print(a)