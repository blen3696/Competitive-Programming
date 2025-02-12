class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
      
        
        if costs[0] > coins:
            return 0

        i = 0
        res = 0
        while i < len(costs) and coins > 0:
            if costs[i] <= coins:
                res += 1
                coins -= costs[i]
            i += 1

        return res


