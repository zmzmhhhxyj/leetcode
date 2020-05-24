class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a1 = [0]*26
        a2 = [0]*26
        count = 0
        for s in s1:
            idx = ord(s)-97
            a1[idx]+=1
        for i,s in enumerate(s2):
            idx = ord(s)-97
            if count<len(s1):
                a2[idx]+=1
                count+=1
            if count==len(s1):
                if a1==a2:
                    return True
                left_idx_s2 = i-len(s1)+1
                left_idx = ord(s2[left_idx_s2])-97
                a2[left_idx]-=1
                count-=1
        return False


x = Solution()
# s1 = "ab" 
# s2 = "eidbaooo"
s1= "ab" 
s2 = "eidboaoo"
ans = x.checkInclusion(s1,s2)
print(ans)