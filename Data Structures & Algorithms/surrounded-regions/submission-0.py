class Solution:
    def solve(self, board: List[List[str]]) -> None:
            row = len(board)
            col = len(board[0])

            def dfs(r, c):
                if r not in range(row) or c not in range(col) or board[r][c] != "O":
                    return

                board[r][c] = "T"

                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

            # Mark all O's connected to the border
            for r in range(row):
                dfs(r, 0)
                dfs(r, col - 1)

            for c in range(col):
                dfs(0, c)
                dfs(row - 1, c)

            # Flip surrounded O's to X
            # Restore border-connected T's back to O
            for r in range(row):
                for c in range(col):
                    if board[r][c] == "O":
                        board[r][c] = "X"
                    elif board[r][c] == "T":
                        board[r][c] = "O"
        