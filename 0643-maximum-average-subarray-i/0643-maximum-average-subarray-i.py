class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        my_sum = sum(nums[:k])
        max_sum = my_sum
        l = 0
        for r in range(k,len(nums)):
            my_sum -= nums[l]
            my_sum += nums[r]
            max_sum = max(max_sum,my_sum)
            l += 1

        return max_sum / k
            

