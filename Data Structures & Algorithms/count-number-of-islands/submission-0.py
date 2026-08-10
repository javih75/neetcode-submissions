class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r, c):
            if r < 0 or r >= len(grid):
                return
            if c < 0 or c >= len(grid[0]):
                return
            if grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(grid, r-1, c)
            dfs(grid, r+1, c)
            dfs(grid, r, c-1)
            dfs(grid, r, c+1)

        counter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dfs(grid, r, c)
                    counter += 1

        return counter