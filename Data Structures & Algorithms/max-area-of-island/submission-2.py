class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        row,col = len(grid),len(grid[0])
        visited=set()
        
        island=0

        def bfs(r,c):
            if r not in range(row) or c not in range(col) or (r,c) in visited or grid[r][c]!=1:
                return 0
            visited.add((r,c))

            return 1+ bfs(r+1,c)+bfs(r-1,c)+bfs(r,c+1)+bfs(r,c-1)




        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and (i,j) not in visited:
                          island = max(island, bfs(i,j)) 

        return island     
        