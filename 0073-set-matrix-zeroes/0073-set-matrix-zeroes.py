class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        row_set=set()
        col_set=set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    row_set.add(i)
                    col_set.add(j)
        for i in range(rows):
            for j in range(cols):
                if i in row_set or j in col_set:
                    matrix[i][j]=0
        
                    
                    
        

        """
        Do not return anything, modify matrix in-place instead.
        """
        