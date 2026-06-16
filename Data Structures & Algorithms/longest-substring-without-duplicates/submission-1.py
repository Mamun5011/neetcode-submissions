class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #initiliaze a set, result and window
        char_set = set()
        res = 0
        l = 0


        #iterate over the characters in string
        for i,c in enumerate(s):
        # check if char is in the set, If yes, continue to remove until it is removed from the set by sliding window
            while c in char_set:
                char_set.remove(s[l])
                l+=1
        # add char to the set
            char_set.add(c)
         # update length
            res = max (res, i-l+1)

        return res




        


       
        