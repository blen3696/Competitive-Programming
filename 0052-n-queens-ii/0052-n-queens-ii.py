class Solution:
    def totalNQueens(self, n: int) -> int:
        columns = set()
        posdiag = set()
        negdiag = set()
        curr = [['.']*n for _ in range(n)]
        res = []
        def backtrack(row):
            if row == n:
                res.append([''.join(r) for r in curr])
                return

            for col in range(n):
                if col not in columns and (col + row) not in posdiag and (col - row) not in negdiag:
                    curr[row][col] = 'Q'
                    columns.add(col)
                    posdiag.add(col + row)
                    negdiag.add(col - row)

                    backtrack(row + 1)

                    curr[row][col] == '.'
                    columns.remove(col)
                    posdiag.remove(col + row)
                    negdiag.remove(col - row)

        backtrack(0)
        return len(res)
