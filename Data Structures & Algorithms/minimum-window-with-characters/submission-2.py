class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # initialize two table for s and t and window

        table_s = collections.defaultdict(int)
        table_t = Counter(t)
        l = 0
        start = 0
        end  = len(s) + 1
        have = 0
        need = len(table_t)
        #Iterate over s
        for i,c in enumerate(s):
            table_s[c] += 1
            #matching with t for the current window of s
            if c in table_t and table_s[c] == table_t[c]:
                have += 1
            while have == need:
                #check current window size and update answer
                if i-l < end - start:
                    start = l
                    end = i
                # Slide the window and see if it fits
                table_s[s[l]] -= 1
                if s[l] in table_t and table_s[s[l]] < table_t[s[l]]:
                    have -= 1
                l+=1
        return s[start:end+1] if end != len(s)+1 else ""


        