import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # initialization
        res = 0
        max_Count = 0
        l = 0
        table = collections.defaultdict(int)

        # go over the string
        for i,c in enumerate(s):
            table[c] += 1
        # update the max count in counter
            max_Count = max (max_Count, table[c])
        # check if replacing covers the current substring unique char (if not update the window)
            while i-l+1 - max_Count > k:
                table[s[l]] -= 1
                l+=1

        #update the resultant length
            res = max(res,i-l+1)
        return res
            

        
        