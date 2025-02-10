class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row = len(image)
        for i in range(row):
            image[i] = image[i][::-1]
        print(image)

        for i in range(row):
            for j in range(row):
                if image[i][j] == 0:
                    image[i][j] = 1
                elif image[i][j] == 1:
                    image[i][j] = 0
        
            
        return image