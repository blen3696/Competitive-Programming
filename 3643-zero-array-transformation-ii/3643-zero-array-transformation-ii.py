class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def validate(m):
            arr = nums[:]
            diff = [0]*(len(nums)+ 1)

            for i in range(m):
                l, r, v = queries[i]
                diff[l] -= v
                diff[r+1] += v

            for i in range(1,len(diff)):
                diff[i] += diff[i - 1]

            for i in range(len(arr)):
                arr[i] += diff[i]

            for i in arr:
                if i > 0:
                    return False
            return True

        l, r = 0, len(queries)
        res = -1
        while l <= r:
            m = (l + r) // 2

            if validate(m):
                res = m
                r = m - 1
            else:
                l = m + 1

        return res