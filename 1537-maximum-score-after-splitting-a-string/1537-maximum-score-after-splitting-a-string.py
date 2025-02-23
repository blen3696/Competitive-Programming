class Solution:
    def maxScore(self, s: str) -> int:
        nums = list(map(int, s))

        for i in range(1,len(nums)):
            nums[i] += nums[i - 1]

        max_score = float('-inf')

        for i in range(len(nums)-1):
            score = ((i + 1 )- nums[i]) + (nums[-1] - nums[i])
            max_score = max(max_score, score)

        return max_score

        