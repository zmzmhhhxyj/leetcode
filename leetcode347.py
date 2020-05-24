import heapq
from typing import List
import collections
class Solution:
    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num]-=1
            else:
                dic[num]=-1
        h = []
        count = 0 
        for key in dic:
            heapq.heappush(h,(dic[key],key)) #dic[key] shows the freq of each num
        res = []
        count = 0
        while count<k:
            freq,num = heapq.heappop(h)
            res.append(num)
            count+=1
        return res

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        # dic = {}
        # for num in nums:
        #     if num in dic:
        #         dic[num]+=1
        #     else:
        #         dic[num]=1
        # h = []
        # for key in dic:
        #     heapq.heappush(h,(dic[key],key)) #dic[key] shows the freq of each num
        #     if len(h)>k:
        #         heapq.heappop(h)
        # res = []
        # while h:
        #     freq,num = heapq.heappop(h)
        #     res.append(num)
        # return res
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
        h = []
        count = 0
        for num in d:
            heapq.heappush(h,(d[num],num))
            count+=1
            if count>k:
                heapq.heappop(h)
                count-=1
        res = []
        while h:
            freq,num = heapq.heappop(h)
            res.append(num)
        return res

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myCounter = collections.Counter(nums)
        res = []
        for k,v in myCounter.most_common(k):
            res.append(k)
        return res
            
nums = [1,1,1,2,2,3]
k = 2
x = Solution()
ans = x.topKFrequent2(nums,k)
print(ans)