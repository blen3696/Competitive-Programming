class Solution:
    def balancedStringSplit(self, s: str) -> int:
        no_r = 0
        no_l = 0
        res = 0

        l = 0
        for r in range(len(s)):
            if s[r] == "R":
                no_r += 1
            elif s[r] == "L":
                no_l += 1
            if no_r == no_l:
                no_r = 0
                no_l = 0
                res += 1
                l = r + 1


        return res

        