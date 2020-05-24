from typing import List
import math
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        l,r = min(nums),max(nums)
        gap = math.ceil((r-l)/(len(nums)-1)) 
        array_min = [float("inf")]*(len(nums)-1)
        array_max = [-float("inf")]*(len(nums)-1)
        for n in nums:
            if n==l or n==r:
                continue
            idx = (n-l)//gap
            array_min[idx] = min(array_min[idx],n)
            array_max[idx] = max(array_max[idx],n)
        maxgap = 0
        prev_num = l
        for bucket in range(len(nums)-1):
            if array_max[bucket]==-float('inf'):
                continue
            cur_num = array_min[bucket]
            maxgap = max(maxgap,cur_num-prev_num)
            prev_num = array_max[bucket]
        maxgap = max(maxgap,r-prev_num)
        return maxgap
        
x = Solution()
# ans = x.maximumGap([0,3,11,19,25,27,28,29,37,50])
# ans = x.maximumGap([1,3,100])
# ans = x.maximumGap([15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740])
a = [12115,10639,2351,29639,31300,11245,16323,24899,8043,4076,17583,15872,19443,12887,5286,6836,31052,25648,17584,24599,13787,24727,12414,5098,26096,23020,25338,28472,4345,25144,27939,10716,3830,13001,7960,8003,10797,5917,22386,12403,2335,32514,23767,1868,29882,31738,30157,7950,20176,11748,13003,13852,19656,25305,7830,3328,19092,28245,18635,5806,18915,31639,24247,32269,29079,24394,18031,9395,8569,11364,28701,32496,28203,4175,20889,28943,6495,14919,16441,4568,23111,20995,7401,30298,2636,16791,1662,27367,2563,22169,1607,15711,29277,32386,27365,31922,26142,8792]
ans = x.maximumGap(a)
print(ans)