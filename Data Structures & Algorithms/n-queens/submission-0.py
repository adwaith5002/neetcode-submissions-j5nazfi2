class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[[""]*n for i in range(n)]
        cols=set()
        posDiag= set()
        negDial= set()
        for i in range(n):
            for j in range(n):
                board[i][j]="."

        def check(board,r):
            if r==n:
                res.append(["".join(row) for row in board])
                return
            for i in range(n):
                if i in cols or (i+r) in posDiag or (r-i) in negDial:
                    continue
                cols.add(i)
                negDial.add(r-i)
                posDiag.add(r+i)
                board[r][i]="Q"
                check(board,r+1)
                cols.remove(i)
                negDial.remove(r-i)
                posDiag.remove(r+i)
                board[r][i]="."
        
        check(board,0)
        return res