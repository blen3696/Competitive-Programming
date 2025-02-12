class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1
        while l < r:
            my_sum = numbers[l] + numbers[r]

            if my_sum == target:
                return [l + 1,r + 1]
            elif my_sum < target:
                l += 1
            else:
                r -= 1
        return []