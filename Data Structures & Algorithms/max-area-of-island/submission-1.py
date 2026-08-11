class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(coord):
            myRow, myCol = coord
            if (
                0 <= myRow < rows and
                0 <= myCol < cols and
                grid[myRow][myCol] == 1
            ):  
                grid[myRow][myCol] = 0
                return 1 + (
                    dfs((myRow + 1, myCol)) + 
                    dfs((myRow, myCol + 1)) + 
                    dfs((myRow - 1, myCol)) + 
                    dfs((myRow, myCol - 1))
                )
            else:
                return 0
        
        maxSize = 0
        for r in range(rows):
            for c in range(cols):
                maxSize = max(maxSize, dfs((r, c)))
        
        return maxSize



        
