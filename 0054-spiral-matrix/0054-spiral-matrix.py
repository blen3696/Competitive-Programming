class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row,col = len(matrix) , len(matrix[0])
        res = []
        count = [0, 0, 0, 0]
        right = True
        left = False
        down = False
        up = False

        j = 0
        i = 0

        while len(res) < row * col:
                if right:
                    while j < col - count[0]:
                        res.append(matrix[i][j])
                        j +=1
                    j -= 1
                    down = True
                    right = False
                    i += 1
                    count[0] += 1

                elif down:
                    while i < row - count[1]:
                        res.append(matrix[i][j])
                        i += 1
                    i -= 1
                    left = True
                    down = False
                    j -= 1
                    count[1] += 1

                elif left:
                    while j > -1 + count[2]:
                        res.append(matrix[i][j])
                        j -=1
                    j += 1
                    up = True
                    left = False
                    i -= 1
                    count[2] += 1

                elif up:
                    while i > 0 + count[3]:
                        res.append(matrix[i][j])
                        i -= 1
                    i += 1
                    right = True
                    up = False
                    j += 1
                    count[3] += 1
            
        return res
                







        