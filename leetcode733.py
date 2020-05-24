from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        num = image[sr][sc]
        visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
        self.fill(image,sr,sc,newColor,visited,num)
        return image
        
    def fill(self,image,r,c,color,visited,num):
        if r<0 or r>=len(image) or c<0 or c>=len(image[0]) or visited[r][c]:
            return
        visited[r][c] = True 
        if image[r][c]==num:
            image[r][c]=color
            self.fill(image,r-1,c,color,visited,num)
            self.fill(image,r+1,c,color,visited,num)
            self.fill(image,r,c-1,color,visited,num)
            self.fill(image,r,c+1,color,visited,num)

x = Solution()
# ans = x.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2)
ans = x.floodFill([[0,0,0],[0,0,0]],0,0,2)
print(ans)