class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        arr = sorted(nums)
        res = []
        for i in range(len(nums)):
            res.append(arr.index(nums[i]))

        return res
            