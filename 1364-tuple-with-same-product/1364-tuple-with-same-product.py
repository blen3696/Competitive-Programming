class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                d[nums[i]*nums[j]] += 1
        
        ctn = 0

        for val in d.values():
            if val > 1:
                ctn += val*(val-1)*4

        return ctn