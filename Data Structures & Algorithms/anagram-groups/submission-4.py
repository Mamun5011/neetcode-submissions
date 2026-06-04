import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table=collections.defaultdict(list)

        for string in strs:
            a = sorted(string)
            table[tuple(a)].append(string)
       
       
        return list(table.values())
