class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        def comparator(a,b):
            if  a + b  > b + a:
                return -1
            else:
                return 1

        nums.sort(key = cmp_to_key(comparator))

        if nums[0] == "0":
            return "0"

        return("".join(nums))