class Solution:
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        l_arr = nums[:mid]
        r_arr = nums[mid:]
        
        l_arr = self.mergeSort(l_arr)
        r_arr = self.mergeSort(r_arr)
        
        return self.merge(l_arr, r_arr)

    def merge(self, l, r):
        res = []
        i = j = 0
        
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1
        
        res.extend(l[i:])
        res.extend(r[j:])
        
        return res

    def sortArray(self, nums: List[int]):
        return self.mergeSort(nums)
        

        
        