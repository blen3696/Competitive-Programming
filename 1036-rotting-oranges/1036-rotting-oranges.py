class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [(0,1), (1,0), (0,-1), (-1,0)]

        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        def in_bound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        queue = deque()
        ctn = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row,col))
                    visited[row][col] = True
                elif grid[row][col] == 1:
                    ctn += 1

        time = 0

        while queue and ctn > 0:
            for _ in range(len(queue)): 
                row, col = queue.popleft()

                for dr, dc in direction:
                    new_row, new_col = row + dr, col + dc

                    if in_bound(new_row, new_col) and not visited[new_row][new_col] and grid[new_row][new_col] == 1:
                        visited[new_row][new_col] = True
                        queue.append((new_row, new_col))
                        ctn -= 1
    
            time += 1


        return  time if ctn == 0 else -1


