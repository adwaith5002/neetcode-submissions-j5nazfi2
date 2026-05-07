class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=set()
        row=len(board)
        cols=len(board[0])

        def search(r, c, i):
            if i ==len(word):
                return True
            if r<0 or c<0 or r>=row or c>= cols or (r,c) in visited or board[r][c]!=word[i]:
                return False
            if board[r][c] == word[i]:
                visited.add((r,c))
                res=(search(r+1,c,i+1) or
                    search(r-1,c,i+1) or
                    search(r,c-1,i+1) or
                    search(r,c+1,i+1))
                visited.remove((r,c))
                return res
        for r in range(row):
            for c in range(cols):
                if search(r,c,0):
                    return True
        return False           