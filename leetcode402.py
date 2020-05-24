class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        if k==len(num):
            return "0"
        for n in num:
            while k>0 and stack and stack[-1]>n:
                stack.pop()
                k-=1
            stack.append(n)
        while k>0:
            stack.pop()
            k-=1
        i = 0
        while stack[i]=="0":
            i+=1
        stack = stack[i:]
        return "".join(stack)
x = Solution()
ans = x.removeKdigits("10200",1)
print(ans)