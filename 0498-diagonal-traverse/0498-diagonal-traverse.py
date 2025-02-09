class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        row, col = len(mat), len(mat[0])
        i, j = 0, 0
        dir = True
        res = []
        
        for _ in range(row * col):
            res.append(mat[i][j])
            
            if dir:
                if j == col - 1:
                    i += 1
                    dir = False
                elif i == 0:
                    j += 1
                    dir = False
                else:
                    i -= 1
                    j += 1
            else:
                if i == row - 1:
                    j += 1
                    dir = True
                elif j == 0:
                    i += 1
                    dir = True
                else:
                    i += 1
                    j -= 1
        
        return res

