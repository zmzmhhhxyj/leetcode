from typing import List

def maximalSquare(matrix: List[List[str]]) -> int:
    num_row = len(matrix)
    num_col = len(matrix[0])
    #matrix_d = [[0 for i in range(num_col)] for k in range(num_row)]
    """     
    for i in range(num_row):
        matrix_d[i][0]=matrix[i][0]
    for i in range(num_col):
        matrix_d[0][i] = matrix[0][i] 
    """
    matrix_d = [[0 if matrix[i][j]=="0" else 1 for j in range(num_col)]for i in range(num_row)]
    for i in range(1,num_row):
        for j in range(1,num_col):
            if matrix[i][j] == '1':
                matrix_d[i][j]=min(matrix_d[i-1][j-1],matrix_d[i-1][j],matrix_d[i][j-1])+1
            else:
                matrix_d[i][j]=0
    num_max=0
    for i in range(num_row):
        for j in range(num_col):
            if matrix_d[i][j]>num_max:
                num_max=matrix_d[i][j]
    return num_max*num_max


#a=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#a=[[1,0,1,0,0],[1,0,1,1,1]]
a=[["1"]]

res=maximalSquare(a)
print(res)