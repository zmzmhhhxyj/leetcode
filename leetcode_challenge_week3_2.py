class Solution:
    def checkValidString(self, s: str) -> bool:
        lstack = []
        starstack = []
        for i in range(len(s)):
            n = s[i]
            if n=="(":
                lstack.append(i)
            elif n=="*":
                starstack.append(i)
            elif n == ")":
                if lstack:
                    lstack.pop()
                elif starstack:
                    starstack.pop()
                else:
                    return False
        while lstack:
            if not starstack:
                return False
            a = lstack.pop()
            b = starstack.pop()
            if a<b:
                continue
            else:
                return False
        return True

x = Solution()
ans = x.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*")
print(ans)

# ((*)(*))((*