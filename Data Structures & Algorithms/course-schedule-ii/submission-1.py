class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = []
        preMap = collections.defaultdict(list)

        for u, v in prerequisites:
            preMap[u].append(v)

        visited = set()   # courses in current DFS path
        done = set()      # courses already fully processed

        def dfs(course):
            if course in visited:
                return False

            if course in done:
                return True

            visited.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            visited.remove(course)

            done.add(course)
            res.append(course)

            return True

        for n in range(numCourses):
            if not dfs(n):
                return []

        return res
        