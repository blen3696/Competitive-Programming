class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        my_sum  = 0
        my_dic = {0:1}
        res = 0

        for num in nums:
            my_sum += num
            reminder = my_sum % k

            res += my_dic.get(reminder, 0)
            my_dic[reminder] = my_dic.get(reminder, 0) + 1
            
        return res