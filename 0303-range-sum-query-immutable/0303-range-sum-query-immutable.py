class NumArray:

    def __init__(self, nums: List[int]):
        self.pri_sum = [0]
        for num in nums:
            self.pri_sum.append(self.pri_sum[-1] + num)
        print(self.pri_sum)

        

    def sumRange(self, left: int, right: int) -> int:
        return self.pri_sum[right + 1] - self.pri_sum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)