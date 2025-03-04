class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        doub_opp = 0
        inc_opp = 0
        res = 0

        while maxDoubles > 0 and target > 1:
            inc_opp += target % 2
            target //= 2
            doub_opp += 1
            maxDoubles -= 1
        res = (target - 1) + doub_opp  + inc_opp

        return res
        
        