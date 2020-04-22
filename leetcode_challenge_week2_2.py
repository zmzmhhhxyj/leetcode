class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = []
        t = []
        for i in range(len(S)):
            if S[i]=="#" and s:
                s.pop()
            elif S[i]!="#":
                s.append(S[i])
        for j in range(len(T)):
            if T[j]=="#" and t:
                t.pop()
            elif T[j]!="#":
                t.append(T[j])
        return s==t

# S = "ab#c"
# T = "ad#c"
# S = "ab##"
# T = "c#d#"
# S = "a##c"
# T = "#a#c"
S = "y#fo##f"
T = "y#f#o##f"
x = Solution()
ans = x.backspaceCompare(S,T)
print(ans)
