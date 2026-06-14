import collections
class TimeMap:

    def __init__(self):
        self.table = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.table[key]) - 1
        if r == -1:
            return ""
        res  = ""

        while l <= r:
            mid  = (l + r)//2
            if self.table[key][mid][1] == timestamp:
                return self.table[key][mid][0]
            elif self.table[key][mid][1] < timestamp:
                res = self.table[key][mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res



        
