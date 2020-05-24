from typing import List
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i,j = 0,0
        while i<len(A) and j<len(B):
            x,y = A[i][0],A[i][1]
            u,v = B[j][0],B[j][1]
            if x<=u:
                if y<u:
                    i+=1
                elif y>=v:
                    j+=1
                    res.append([u,v])
                elif y<v:
                    i+=1
                    res.append([u,y])
            else:
                if v<x:
                    j+=1
                elif v>=y:
                    i+=1
                    res.append([x,y])
                elif v<y:
                    j+=1
                    res.append([x,v])
        return res

A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
x = Solution()
res = x.intervalIntersection(A,B)
print(res)