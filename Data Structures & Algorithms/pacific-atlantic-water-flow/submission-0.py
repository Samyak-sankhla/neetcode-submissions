from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac_que=deque()
        atl_que=deque()
        pac_seen=set()
        atl_seen=set()

        m, n = len(heights), len(heights[0])
        for i in range(m):
            pac_que.append((i,0))
            atl_que.append((i,n-1))
            pac_seen.add((i,0))
            atl_seen.add((i,n-1))
        for j in range(1,n):
            pac_que.append((0,j))
            pac_seen.add((0,j))
        for j in range(n-1):
            atl_que.append((m-1,j))
            atl_seen.add((m-1,j))
        
        def bfs(que,seen):
            while que:
                (i,j)=que.popleft()
                for i_off, j_off in [(0,1),(1,0),(-1,0),(0,-1)]:
                    r,c = i+i_off, j+j_off
                    if 0<=r<m and 0<=c<n and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                        que.append((r,c))
                        seen.add((r,c))
        bfs(pac_que,pac_seen)
        bfs(atl_que,atl_seen)
        return list(pac_seen.intersection(atl_seen))

                   


        