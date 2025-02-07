class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        my_dic = defaultdict(list)
        res = []
        for path in paths:
            root = path.split()
            for i in range(1,len(root)):
                file_name = root[i].split("(")
                my_dic[file_name[1]].append(root[0] + "/" + file_name[0])
        
        for key,val in my_dic.items():
            if len(val) > 1:
                res.append(val)

        return res