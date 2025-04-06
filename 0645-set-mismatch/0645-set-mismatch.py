class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = -1
        m = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                res = nums[i]
            elif nums[i] > nums[i - 1] + 1:
                m = nums[i - 1] + 1

        if nums[-1] != len(nums):
            m = len(nums) if m == 1 else m

        return [res, m]