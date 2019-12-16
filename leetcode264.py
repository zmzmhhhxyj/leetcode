class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        id2,id3,id5=0,0,0
        f2,f3,f5=2,3,5
        for i in range(1,n):
            num_min = min(f2,f3,f5)
            ugly.append(num_min)
            if num_min == f2:
                id2 = id2+1
                f2 = ugly[id2]*2
            if num_min == f3:
                id3 = id3+1
                f3 = ugly[id3]*3
            if num_min == f5:
                id5 = id5+1
                f5 = ugly[id5]*5
        return ugly[-1]

solution = Solution()
a = solution.nthUglyNumber(10)
print(a)