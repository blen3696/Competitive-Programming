class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        pri_sum = [nums[0]]

        for num in nums[1:]:
            pri_sum.append(pri_sum[-1] + num)

        return pri_sum

        