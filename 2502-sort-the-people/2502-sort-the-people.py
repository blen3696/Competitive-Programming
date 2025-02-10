class Solution:
    def sortPeople(self, names: List[str], height: List[int]) -> List[str]:
        n = len(height)

        for i in range(n):
            for j in range(1, n - i):
                if height[j] > height[j - 1]:
                    height[j], height[j - 1] = height[j - 1], height[j]
                    names[j], names[j - 1] = names[j - 1], names[j]

        return names