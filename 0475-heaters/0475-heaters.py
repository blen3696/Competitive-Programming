class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        def validate(m):
            l = 0
            for heat in heaters:
                while l < len(houses) and heat - m <= houses[l] <= heat + m:
                        l += 1
               
            return l == len(houses) 

        
        houses.sort()
        heaters.sort()
        
        l, r = 0, max(max(houses), max(heaters))

        while l <= r:
            m = (l + r)// 2

            if validate(m):
                r = m - 1
            else:
                l = m + 1

        return l

