class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_ones = 0
        zeros = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            else:
                max_ones = max(max_ones,r - l + 1)
                
        return max_ones

        