class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
       
        pre_sum = [0]
        for i in range(len(nums)):
            pre_sum.append(pre_sum[-1]  + nums[i])

      

        for i in range(1,len(pre_sum)):
            if pre_sum[i -1] == (pre_sum[-1] - pre_sum[i]):
                return i - 1
        

        return  -1
        