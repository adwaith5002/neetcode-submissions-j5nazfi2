class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        border=set()
        for i in range(len(board)):

            if board[i][0]=='O':
                border.add((i,0))
            if board[i][len(board[0])-1]=='O':
                border.add((i,len(board[0])-1))
        for j in range(len(board[0])):
            if board[0][j]=='O':
                border.add((0,j))
            if board[len(board)-1][j]=='O':
                border.add((len(board)-1,j))
            
        def dfs(r,c):
            if r<0 or c<0 or r==len(board) or c==len(board[0]) or board[r][c]=='X' or board[r][c]=='#':
                return
            board[r][c]='#'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for i,j in border:
            dfs(i,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='#':
                    board[i][j]='O'
                