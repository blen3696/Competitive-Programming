class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        my_sum = 0

        for i in range(k):
            happy = happiness[i] - i
            if happy < 0:
                pass
            else:
                my_sum += happy
        return my_sum
