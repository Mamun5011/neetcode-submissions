class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))
            res+="#"+s
        return res

    def decode(self, s: str) -> List[str]:
        l = 0
        size = len(s)
        res=[]

        while l<size:
            r = s.find("#",l)
            sz = int(s[l:r])
            l = r+1
            res.append(str(s[l:l+sz]))
            l+=sz
        return res

