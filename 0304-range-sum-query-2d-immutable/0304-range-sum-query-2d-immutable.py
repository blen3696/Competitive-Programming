class NumMatrix:

    def __init__(self, mat: List[List[int]]):
        my_sum = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i and j:
                    mat[i][j] += mat[i - 1][j] + mat[i][j - 1] - mat[i - 1][j - 1] 

                elif i:
                    mat[i][j] += mat[i -1][j]

                elif j:
                    mat[i][j] += mat[i][j - 1]
        self.matrix = mat
        print(self.matrix)
            

        

        

    def sumRegion(self, i: int, j: int, k: int, m: int) -> int:
        if i and j:
            return self.matrix[k][m] - self.matrix[i - 1][m] - self.matrix[k][j - 1] + self.matrix[i -1][j - 1]
        elif i:
            return self.matrix[k][m] - self.matrix[i - 1][m]
        elif j:
            return self.matrix[k][m] - self.matrix[k][j - 1]

        else:
            return self.matrix[k][m]

        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)