class Solution:
    def maskPII(self, s: str) -> str:
        s1 = set(s)

        if "@" in s1:
           char1,char2 = s.split('@')
           res = char1[0] + "*****" + char1[-1] + "@" + char2
           return res.lower()

        else:
            su = re.sub(r"\D", "",s)

            size = len(su)
            local = "***-***-" + su[size-4:]

            if size > 10:
                cun_code = "+" + "*"*(size-10)

                return cun_code + "-" + local
            else:
                return local



        



            