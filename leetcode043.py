class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        cnum2 = 0
        cnum1 = 0
        for i,value in enumerate(num2[::-1]):
            tmp = 10**i
            cnum2+=tmp*int(value)
        for i,value in enumerate(num1[::-1]):
            tmp = 10**i
            cnum1+=tmp*int(value)
        
        return str(cnum2*cnum1)

x = Solution()
res = x.multiply('2','115')
print(res)