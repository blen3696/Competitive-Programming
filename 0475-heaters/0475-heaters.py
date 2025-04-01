class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def validator(m):
            i, j = 0, 0
            while i < len(houses) and j < len(heaters):
                if abs(houses[i] - heaters[j]) <= m:
                    i += 1  
                else:
                    j += 1 
            return i == len(houses)  
        
        houses.sort()
        heaters.sort()
        l, r = 0, max(max(houses) - min(heaters), max(heaters) - min(houses))
        
        while l <= r:
            m = (l + r) // 2
            if validator(m):
                r = m - 1
            else:
                l = m + 1
        
        return l

