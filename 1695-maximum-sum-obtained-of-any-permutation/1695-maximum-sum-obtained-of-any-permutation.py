class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        my_dic = [0]*(len(nums) + 1)

        for l, r in requests:
            my_dic[l] += 1
            my_dic[r + 1] -= 1
        for i in range(1, len(my_dic)):
            my_dic[i] += my_dic[ i - 1]

        my_dic.sort(reverse=True)
        nums.sort(reverse = True)
        res = 0
        for i,j in zip(my_dic,nums):

            res+= i*j

        return res%(10**9 +7)