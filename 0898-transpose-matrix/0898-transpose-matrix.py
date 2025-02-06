class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        row,col =  len(matrix),len(matrix[0])
        print(row)
        print(col)
        res = []
        for i in range(row):
            for j in range(col):
                r = [0]* row
                res.append(r)

        for i in range(row):
            for j in range(col):
                res[j][i] = matrix[i][j]
        arr = []

        for i in range(col):
            arr.append(res[i])

         

                

        return arr

        