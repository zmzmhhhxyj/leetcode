from typing import List
class Solution:
    def generateMatrix(self, n): 
        """ 
        :type n: int
        :rtype: List[List[int]]
        """
        res, lo = [[n*n]], n*n 
        while lo > 1:
            lo, hi = lo - len(res), lo
            #print('res:', res)
            list2 =  [list(j) for j in zip(*res[::-1])]
            print("res:",res," zip(*res[::-1]):",list(zip(*res[::-1]))," zip(*res)",list(zip(*res))," zip(res[::-1]):",list(zip(res[::-1])))
            res = [[i for i in range(lo, hi)]] + list2
        return res 

x = Solution()
a = x.generateMatrix(3)
print(a)