class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N<=9:
            return N
        s = str(N)
        idx = 0
        last = len(s)-2
        while idx<=last:
            if s[idx]>s[idx+1]:
                l = len(s)-idx-1
                backs = str('9'*l)
                s = s[:idx]+str(int(s[idx])-1)+backs
                idx = max(0,idx-1)
                last = idx
            else:
                idx+=1      
        return int(s)
        
    def monotoneIncreasingDigits2(self,N):
        S = list(str(N))
        i = 1
        while i < len(S) and S[i-1] <= S[i]:
            i += 1
        while 0 < i < len(S) and S[i-1] > S[i]:
            S[i-1] = str(int(S[i-1]) - 1)
            i -= 1
        S[i+1:] = '9' * (len(S) - i-1)
        return int("".join(S))

x = Solution()
ans = x.monotoneIncreasingDigits2(44426)
print(ans)