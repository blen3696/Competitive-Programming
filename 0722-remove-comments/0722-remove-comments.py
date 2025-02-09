class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        res = []
        s = []
        flag = False

        for code in source:
            i = 0
            while i < len(code):
                if not flag:
                    if i + 1 < len(code) and code[i:i+2] == "/*":
                        flag = True
                        i += 1
                    elif i + 1 < len(code) and code[i:i+2] == "//":
                        break
                    else:
                        s.append(code[i])
                else:
                    if i + 1 < len(code) and code[i:i+2] == "*/":
                        flag = False
                        i += 1
                i +=1
        
            if s and not flag:
                res.append("".join(s))
                s = []
        
        return res

                    
