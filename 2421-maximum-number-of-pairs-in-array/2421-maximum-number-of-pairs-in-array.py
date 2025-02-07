class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        my_dic = Counter(nums)
        ctn1 = 0
        ctn2 = 0

        for key, val in my_dic.items():
            if val%2 == 0:
                ctn1 += val//2
            elif val% 2 != 0 and val > 1:
                num = val -1
                ctn2 += 1
                ctn1 += num//2
            elif val == 1:
                ctn2 += 1
        return [ctn1,ctn2]
