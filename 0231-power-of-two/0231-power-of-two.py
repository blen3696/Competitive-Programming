class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def helper(n):
            if n < 1:
                return False
            if n == 1:
                return True
            return helper(n/2)

        return helper(n)
        