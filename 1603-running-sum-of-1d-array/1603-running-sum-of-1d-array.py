class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        pri_sum = []
        s = 0


        for num in nums:
            s += num
            pri_sum.append(s)

        return pri_sum
        
        