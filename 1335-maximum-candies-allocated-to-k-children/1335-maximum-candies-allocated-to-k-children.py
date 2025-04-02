class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        def validate(m):
            ctn = 0
            for i in candies:
                ctn += math.floor(i/m)

            return ctn >= k



        l, r = 1 , max(candies)
        res = 0
        while l <= r:
            m = (l + r) // 2

            if validate(m):
                res = m
                l = m + 1
            else:
                r = m - 1
        return res