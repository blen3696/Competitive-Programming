class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        window = sum(nums[:3])
        res = 0
        if (window- nums[2]) > nums[2]:
            res = window

        for i in range(3,len(nums)):
            window -= nums[i - 3]
            window += nums[i]

            if (window- nums[i]) > nums[i]:
                res = window
        return res
        





        