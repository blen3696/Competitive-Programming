class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque()
        max_q = deque()
        l = 0
        max_len = 0

        for r in range(len(nums)):
            while min_q and min_q[-1] < nums[r]:
                min_q.pop()
            min_q.append(nums[r])
            while max_q and max_q[-1] > nums[r]:
                max_q.pop()
            max_q.append(nums[r])

            while min_q[0] - max_q[0] > limit:
                n = nums[l]
                if min_q[0] == n:
                    min_q.popleft()
                if max_q[0] == n:
                    max_q.popleft()

                l += 1
            max_len = max(max_len, r - l + 1)

        return max_len


