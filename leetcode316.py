import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count, visit = [0]*len(s),[False]*len(s)
        ans =  []
        for c in s:
            count[ord(c)-97] += 1
        for c in s:
            count[ord(c)-97] -= 1
            if visit[ord(c)-97]:
                continue
            while ans and ans[-1]>c and count[ord(ans[-1])-97]>0:
                visit[ord(ans.pop())-97] = False
            ans.append(c)
            visit[ord(c)-97] = True
        return "".join(ans)

    def removeDuplicateLetters2(self, s):
        d = {}
        ans = []
        for i, value in enumerate(s):
            d[value] = i
        for k in range(len(s)):
            if s[k] not in ans:
                while ans and ans[-1]>s[k] and d[ans[-1]]>k:
                    ans.pop()
                ans.append(s[k])
        return "".join(ans)

x = Solution()
res = x.removeDuplicateLetters2("cbacdcbc")
print(res)