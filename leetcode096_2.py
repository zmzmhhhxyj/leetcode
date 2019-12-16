class Solution:
    def numTrees(n: int) -> int:
        T = [1,1,2]+[0]*(n-2)
        for m in range(3,n+1):
            for i in range(m):
                T[m] += T[i]*T[m-i-1]
        return T[-1]

a = Solution.numTrees(3)
print(a)