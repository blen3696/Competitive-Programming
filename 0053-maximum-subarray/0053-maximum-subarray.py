class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        my_sum = 0

        for i in range(len(nums)):
            my_sum += nums[i]

            max_sum = max(max_sum, my_sum)

            if my_sum < 0:
                my_sum = 0

        return max_sum 
    