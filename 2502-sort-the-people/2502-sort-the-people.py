class Solution:
    def sortPeople(self, names: List[str], height: List[int]) -> List[str]:
        n = len(height)

        for i in range(n):
            min_index = i
            for j in range(i + 1,n):
                if height[j] >  height[min_index]:
                    min_index = j
            height[i], height[min_index] = height[min_index], height[i]
            names[i], names[min_index] = names[min_index], names[i]


        return names