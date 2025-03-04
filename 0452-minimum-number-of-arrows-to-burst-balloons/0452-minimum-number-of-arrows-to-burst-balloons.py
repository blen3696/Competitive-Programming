class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = 1
        print(points)

        l = 0
        r = 1
        max_min = points[l][0]
        min_max = points[l][1]
        while r < len(points):
            if points[l][1] < points[r][0]:
                l = r
                r += 1
                res += 1
                max_min = points[l][0]
                min_max = points[l][1]

            else:
                max_min = max(max_min,points[r][0])
                min_max = min(min_max,points[r][1])
                if max_min > min_max:
                    l = r
                    res += 1
                    max_min = points[l][0]
                    min_max = points[l][1]
                r += 1

        return res


        