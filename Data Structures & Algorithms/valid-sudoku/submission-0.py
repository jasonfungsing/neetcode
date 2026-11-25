class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        cubes = [[set() for _ in range(3)] for _ in range(3)]
        
        for row, rv in enumerate(board):
            for col, cv in enumerate(rv):
                if cv != ".":

                    if cv in rows[row]:
                        return False
                    else:
                        rows[row].add(cv)

                    if cv in cols[col]:
                        return False
                    else:
                        cols[col].add(cv)

                    if cv in cubes[row//3][col//3]:
                        return False
                    else:
                        cubes[row//3][col//3].add(cv)
        return True