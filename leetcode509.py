class Solution:
    f = []
    def fib(self, N: int) -> int:
        f = [0]*(N+1)
        def rec(N):
            if N==0:
                return 0
            if N==1:
                return 1
            f[N] = rec(N-1)+rec(N-2)
            return f[N]
        rec(N)
        return f[N]

x = Solution()
ans = x.fib(4)
print(ans)