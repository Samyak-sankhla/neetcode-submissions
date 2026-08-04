from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        q=deque()
        fresh_count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count+=1
                elif grid[i][j] == 2:
                    q.append((i,j))
        if fresh_count == 0:
            return 0
        minutes=-1
        while q:
            size=len(q)
            minutes+=1
            for _ in range(size):
                i,j = q.popleft()
                for i_off, j_off in [(0,1),(1,0),(0,-1),(-1,0)]:
                    r,c=i+i_off, j+j_off
                    if 0 <=r<m and 0<=c<n and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r,c))
                        fresh_count-=1
        if fresh_count > 0:
            return -1
        return minutes