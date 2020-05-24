class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        f = [1]*n
        nums = []
        res = []
        for i in range(2,n):
            f[i] = f[i-1]*i
        for i in range(1,n+1):
            nums.append(i)
        k-=1
        for i in range(n-1,-1,-1):
            idx = k//f[i]
            k = k%f[i]
            res.append(str(nums[idx]))
            nums.remove(nums[idx])
        return "".join(res)

    def getPermutation2(self, n: int, k: int) -> str:
        if n==1:
            return "1"
        res = []
        self.k = k
        self.dfs(n,[],res)
        res = res[0]
        return "".join(res)
    def dfs(self,n,path,res):
        if len(path)==n:
            self.k-=1
            if self.k==0:
                res.append(path.copy())
                #res = path.copy()
            return
        for i in range(1,n+1):
            if str(i) not in path:
                path.append(str(i))
                self.dfs(n,path,res)
                path.pop()

x = Solution()
res = x.getPermutation(3,3)
print(res)