class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def in_bound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))


        def dfs(row, col):
            para = 0

            visited[row][col] = True
            for row_c, col_c in dir:
                new_r, new_c = row + row_c, col + col_c
                if not in_bound(new_r, new_c) or grid[new_r][new_c] == 0:
                    para += 1
                elif not visited[new_r][new_c]:
                    para += dfs(new_r, new_c)
            return para

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return dfs(row, col)


        return 0 
                


