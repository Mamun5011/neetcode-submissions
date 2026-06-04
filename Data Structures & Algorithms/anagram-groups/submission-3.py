import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table=collections.defaultdict(list)

        for str1 in strs:
            a = sorted(str1)
            table[tuple(a)].append(str1)
       
       
        return list(table.values())
