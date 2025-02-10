class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        max_val = max(nums)

        count = [0]* (max_val + 1)

        for num in nums:
            count[num] += 1

        i = 0
        for idx,frq in enumerate(count):
            for _ in range(frq):
                nums[i] = idx
                i += 1
     

