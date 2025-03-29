class TimeMap:

    def __init__(self):
        self.my_dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.my_dic:
            self.my_dic[key] = []
        self.my_dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_dic:
            return ""
        
        values = self.my_dic[key]
        idx = bisect.bisect_right(values, (timestamp, chr(127)))

        if idx == 0:
            return ""
        
        return values[idx - 1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)