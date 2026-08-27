class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col  = len(grid[0])

        q = deque()
        res = 0
        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] ==1:
                    fresh+=1
        while q:
            size  = len(q)
            flag = False
            for i in range(size):
                r,c = q.popleft()
                for xr, xc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if xr not in range(row) or xc not in range(col) or grid[xr][xc] != 1:
                        continue;
                    grid[xr][xc] = 2
                    fresh-=1
                    q.append((xr,xc))
                    flag = True
            if flag:
                res+=1
        return res if fresh==0 else -1

        