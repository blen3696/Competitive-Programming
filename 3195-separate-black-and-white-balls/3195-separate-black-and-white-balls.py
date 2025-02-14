class Solution:
    def minimumSteps(self, s: str) -> int:
        l = 0
        swap = 0
        res = 0
        for r in range(len(s) - 1,-1,-1):
            if s[r] == "0":
                swap += 1
            elif s[r] == "1":
                res += swap
            

        return res
            
        