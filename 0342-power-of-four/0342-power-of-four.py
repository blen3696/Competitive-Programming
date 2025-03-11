class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def power_four(n):
            if n < 1:
                return False
            if n == 1:
                return True

            n = n/4
            return power_four(n)

        return power_four(n)

        