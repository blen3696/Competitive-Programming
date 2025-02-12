class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_val = max(costs)
        counts = [0]*(max_val + 1)

        for num in costs:
            counts[num] += 1

        ctn = 0
        for idx, frq in enumerate(counts):
            for _ in range(frq):
                costs[ctn] = idx
                ctn += 1
      

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


