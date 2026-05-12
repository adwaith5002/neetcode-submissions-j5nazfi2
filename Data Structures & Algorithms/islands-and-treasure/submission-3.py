class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()
        visited=set()

        def add(r,c):
            if(r<0 or c<0 or r==len(grid) or c==len(grid[0]) or (r,c) in visited or grid[r][c]==-1):
                return
            visited.add((r,c))
            q.append((r,c))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    q.append((i,j))
                    visited.add((i,j))
        dist=0
        while q:
            n=len(q)
            for i in range(n):
                r,c=q.popleft()
                grid[r][c]=dist
                add(r+1,c)
                add(r-1,c)
                add(r,c+1)
                add(r,c-1)
            dist+=1

                    

