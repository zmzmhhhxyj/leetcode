class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)<=numRows or numRows==1:
            return s
        index,step = 0,1
        l = [""]*numRows
        for x in s:
            l[index] += x
            if index==0:
                step = 1
            if index==numRows-1:
                step = -1
            index+=step
        return "".join(l)

x = Solution()
res = x.convert("ABC",1)
print(res)