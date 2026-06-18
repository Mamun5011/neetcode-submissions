class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #initialize window start point and end point
        l = 0
        r = len(s1)

        s1_freq = Counter(s1)


        #iterate over s2 and search for same frequency
        while r <= len(s2):
            if Counter(s2[l:r]) == s1_freq:
                return True
            r += 1
            l += 1
        return False
        