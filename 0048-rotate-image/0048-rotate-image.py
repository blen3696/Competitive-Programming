class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row= len(mat)
        for i in range(row):
            for j in range(i + 1,row):
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
        print(mat)
        
        for i in range(row):
            mat[i].reverse()

       