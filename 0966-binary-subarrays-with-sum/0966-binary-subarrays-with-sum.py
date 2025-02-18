class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        my_dic  = { 0:1}
        pre_sum = 0
        res = 0

        for num in nums:
            pre_sum += num

            diff = pre_sum - goal
            res += my_dic.get(diff,0)

            my_dic[pre_sum] = my_dic.get(pre_sum, 0) + 1

        return res

    
        