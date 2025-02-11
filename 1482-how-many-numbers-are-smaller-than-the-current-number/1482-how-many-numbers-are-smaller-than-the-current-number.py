class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # [ 1,2,2,3,8] [8,1,2,2,3]

        arr = sorted(nums)
        res = []
        for i in range(len(nums)):
            res.append(arr.index(nums[i]))

        return res
            