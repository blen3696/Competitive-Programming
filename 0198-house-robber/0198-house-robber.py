class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(n):
            if n < 0:
                return 0
            elif n not in memo:
                memo[n] = max(dp(n-1), dp(n-2) + nums[n])
            return memo[n]

        return dp(len(nums) - 1)