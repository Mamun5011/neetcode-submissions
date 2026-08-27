class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        row,col = len(grid),len(grid[0])
        q = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i,j))
        while q:
            r,c = q.popleft()

            for xr,xc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if xr not in range(row) or xc not in range(col) or grid[xr][xc] != 2147483647:
                    continue
                grid[xr][xc] = 1 + grid[r][c]
                q.append((xr,xc))
        
                     

     