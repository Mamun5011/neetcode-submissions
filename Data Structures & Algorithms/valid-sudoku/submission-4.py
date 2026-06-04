import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_table=collections.defaultdict(list)
        col_table= collections.defaultdict(list)
        square_table=collections.defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!=".":
                    if board[i][j] in row_table[i]:
                       return False
                    else: 
                        row_table[i].append(board[i][j])
                    
                    if board[i][j] in col_table[j]:
                        return False
                    else:
                        col_table[j].append(board[i][j])

                    if board[i][j] in square_table[(i//3,j//3)]:
                        return False
                    else:
                        square_table[(i//3,j//3)].append(board[i][j])
                
        return True
