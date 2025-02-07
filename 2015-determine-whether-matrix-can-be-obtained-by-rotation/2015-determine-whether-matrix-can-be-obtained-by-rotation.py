class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        row,col =  len(mat),len(mat[0])
        for _ in range(4):
            if mat == target: return True 
            mat = [list(row) for row in zip(*mat[::-1])]
        return False
        """print(arr)

        for char in arr:
                l = 0
                r = len(char)-1

                while l < r:
                    char[l],char[r] = char[r], char[l]
                    l +=1
                    r -=1

        print(arr)
        if arr == target:
            return True
        else:
            arr = [list(row) for row in zip(*mat)]
            print(arr)
            if arr == target:
                return True

        return False"""