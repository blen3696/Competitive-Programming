class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def validate(m):
            ctn = 0
            for r in ranks:
                n = math.floor(math.sqrt(m / r))
                ctn += n
            
            return ctn >= cars
                  
        l, r = 1, max(ranks)*(cars**2)
        res = -1
        while l <= r:
            m = (l + r) // 2
            if validate(m):
                r = m - 1
            else:
                l = m + 1
        return l