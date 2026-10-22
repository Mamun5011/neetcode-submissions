class Solution:
    def isPalindrome(self, s: str) -> bool:

        l=0
        r=len(s) - 1
        s = s.lower()

        while l < r:
            while l < r and not self.isAlphanumeric(s[l]):
                l+= 1
            while l < r and not self.isAlphanumeric(s[r]):
                r-= 1
            if s[l] != s[r]:
                print(l,r)
                return False
            l+=1
            r-=1
           
        return True
        

    def isAlphanumeric(self,s):
        return ord('a')<=ord(s)<=ord('z') or ord('A')<=ord(s)<=ord('Z') or ord('0')<=ord(s)<=ord('9')