class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_el = nums[r]
        while l <= r:
            m = ( l + r ) // 2

            if nums[m] < min_el:
                min_el = nums[m]
                r = m - 1
            else:
                l = m + 1

        return min_el
