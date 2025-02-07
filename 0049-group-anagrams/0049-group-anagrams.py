class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dic = defaultdict(list)
        res =[]

        for word in strs:
            key = ''.join(sorted(word))
            my_dic[key].append(word)

        for key, val in my_dic.items():
            res.append(val)

        return res
