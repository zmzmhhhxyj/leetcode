from  typing import List 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        if len(height)<2:
            return 0
        for high in range(1,len(height)):
            for low in range(high-1,-1,-1):
                area = min(height[low],height[high])*(high-low)
                if area>max_area:
                    max_area = area
        return max_area

x = Solution()
a = x.maxArea([1,8,6,2,5,4,8,3,7])
print(a)