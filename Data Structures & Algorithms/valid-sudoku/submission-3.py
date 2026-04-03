class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            row_seen=set()
            for column in range(9):
                if board[row][column] == ".":
                    continue
                if board[row][column] in row_seen:
                    return False
                row_seen.add(board[row][column])
        for column in range(9):
            column_seen=set()
            for row in range(9):
                if board[row][column] == ".":
                    continue
                if board[row][column] in column_seen:
                    return False
                column_seen.add(board[row][column])
        for square in range(9):
            three_seen=set()
            for i in range(3):
                for j in range(3):
                    row=(square//3)*3+i
                    column =(square % 3)*3+j
                    if board[row][column] == ".":
                        continue
                    if board[row][column] in three_seen:
                        return False
                    three_seen.add(board[row][column])
        return True