from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0]*26
        for task in tasks:
            freq[ord(task)-65]+=1
        freq_max = max(freq)
        rest = 0
        for freq_ in freq:
            if freq_==freq_max:
                rest+=1
        count = (freq_max-1)*(n+1)+rest
        return max(count,len(tasks))
        

a = ["A","A","A","B","B","B"]
x = Solution()
res = x.leastInterval(a,2)
print(res)