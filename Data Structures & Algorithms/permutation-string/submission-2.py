class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #validity check
        if len(s1) > len(s2):
            return False

        #initialize window
        l = 0
        r = len(s1)

        
        # counter for both s1 and substr of s2
        s1_freq = Counter(s1)
        s2_freq = Counter(s2[l:r])


        #iterate over s2 and search for same frequency
        while r <= len(s2):
            if s2_freq == s1_freq:
                return True
            s2_freq[s2[l]] -= 1

            if r < len(s2):
               s2_freq[s2[r]] += 1 
            l+=1
            r+=1
        return False
        