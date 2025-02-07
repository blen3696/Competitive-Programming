class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        my_dic = { }
        res = []

        for char in cpdomains:
            visit, sub_dom = char.split()
            domain= sub_dom.split(".")
            ctn = int(visit)


            for i in range(len(domain)):
                sub = ".".join(domain[i:])
                my_dic[sub] = my_dic.get(sub,0) + ctn

           
         
        print(my_dic)
        for key,val in my_dic.items():
            res.append(f"{val} {str(key)}")

        return res
        


            

           
            
