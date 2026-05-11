class Node:
    def __init__(self,n):
        self.left=None
        self.right=None
        self.val=n

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        group=0
        def dfs(r,c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]=="0":
                return
            else:
                grid[r][c]="0"
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c-1)
                dfs(r,c+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    dfs(i,j)
                    group+=1
        return group