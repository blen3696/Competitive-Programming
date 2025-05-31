class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        target_sum = total_sum - x
        n = len(nums)

        if target_sum < 0:
            return -1

        max_len = -1
        left = 0
        current_sum = 0

        for right in range(n):
            current_sum += nums[right]

            while current_sum > target_sum and left <= right:
                current_sum -= nums[left]
                left += 1

            if current_sum == target_sum:
                window_length = right - left + 1
                max_len = max(max_len, window_length)

        return n - max_len if max_len != -1 else -1
