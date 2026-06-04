import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_table=collections.defaultdict(set)
        col_table= collections.defaultdict(set)
        square_table=collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!=".":
                    if board[i][j] in row_table[i]:
                       return False
                    else: 
                        row_table[i].add(board[i][j])
                    
                    if board[i][j] in col_table[j]:
                        return False
                    else:
                        col_table[j].add(board[i][j])

                    if board[i][j] in square_table[(i//3,j//3)]:
                        return False
                    else:
                        square_table[(i//3,j//3)].add(board[i][j])
                
        return True
