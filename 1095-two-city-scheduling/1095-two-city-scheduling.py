class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        my_arr = []
        i = 0
        for a,b in costs:
            my_arr.append([a - b, i])
            i += 1
        my_arr.sort()

        my_sum = 0

        for i in range(len(my_arr)//2):
            my_sum += costs[my_arr[i][1]][0]
        for i in range(len(my_arr)//2, len(my_arr)):
            my_sum += costs[my_arr[i][1]][1]

        return my_sum
        


