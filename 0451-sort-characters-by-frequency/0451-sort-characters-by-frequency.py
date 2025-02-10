class Solution:
    def frequencySort(self, s: str) -> str:
        s = list(s)
        my_dic = Counter(s)

        def comparator(char):
            return (my_dic[char],char)

        s.sort(key = comparator, reverse = True)

        return "".join(s)