class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        rows=len(grid)
        cols=len(grid[0])
        def dfs(r,c):
            if r<0 or r>rows-1 or c<0 or c>cols-1:
                return 0
            if grid[r][c] == 0:
                return 0
            if grid[r][c] == 1:
                grid[r][c] =  0
            
            return 1 + dfs(r-1,c)+ dfs(r,c-1)+ dfs(r+1,c)+ dfs(r,c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curr_max=dfs(r,c)
                    max_area=max(max_area,curr_max)

        return max_area

            
        