from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = Counter(nums)
        size = len(nums)
        #res = [[] for i in range(size+1)]
        res=collections.defaultdict(list)
        for key,value in table.items():
            res[value].append(key)
        ans=[]
        count=0
        for i in range(size,0,-1):
            for n in res[i]:
                ans.append(n)
                count+=1
                if count==k:
                    return ans



        