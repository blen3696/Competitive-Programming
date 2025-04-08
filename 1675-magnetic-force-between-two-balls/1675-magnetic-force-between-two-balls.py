class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def validate(n):
            l = 0
            ctn = 1 
            for r in range(1, len(position)):
                if abs(position[r] - position[l]) >= n:
                    l = r
                    ctn += 1
                if ctn == m:
                    return True

            return False

        position.sort()
        l, r = 1, max(position) - min(position)
        res = 0
        while l <= r:
            mid = (l + r)//2

            if validate(mid):
                l = mid + 1
                res = mid
            else:
                r = mid - 1

        return res