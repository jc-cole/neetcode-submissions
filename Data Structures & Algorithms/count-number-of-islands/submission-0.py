class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        toExplore = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    toExplore.add((row, col))

        def dfs(coord):
            myRow, myCol = coord

            toCheck = [
                (myRow + 1, myCol),
                (myRow, myCol + 1),
                (myRow - 1, myCol),
                (myRow, myCol - 1)
            ]

            for row, col in toCheck:
                if (
                    0 <= row < len(grid) and 
                    0 <= col < len(grid[0]) and
                    (row, col) in toExplore
                ):
                    toExplore.remove((row, col))
                    dfs((row, col))
        
        numIslands = 0

        while toExplore:
            dfs(toExplore.pop())
            numIslands += 1

        return numIslands

        
