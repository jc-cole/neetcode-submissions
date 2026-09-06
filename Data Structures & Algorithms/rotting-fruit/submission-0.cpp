class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<tuple<int, int, int>> frontier;
        // row, col, timestamp

        int M = grid.size();
        int N = grid[0].size();

        // put all rotting fruits on frontier
        for (int r = 0; r < M; r++) {
            for (int c = 0; c < N; c++) {
                if (grid[r][c] == 2) {
                    frontier.push({r, c, 0});
                }
            }
        }

        vector<pair<int, int>> deltas = {
            {1, 0},
            {0, 1},
            {-1, 0},
            {0, -1}
        };

        int latestTime = 0;

        while (!frontier.empty()) {
            auto [row, col, timestamp] = frontier.front();
            frontier.pop();

            latestTime = max(latestTime, timestamp);

            for (auto [drow, dcol] : deltas) {
                int newRow = row + drow;
                int newCol = col + dcol;
                if (0 <= newRow && newRow < M && 
                    0 <= newCol && newCol < N &&
                    grid[newRow][newCol] == 1
                ) {
                    grid[newRow][newCol] = 2;
                    frontier.push({newRow, newCol, timestamp + 1});
                }
            }
        }

        // check for fresh fruits and return -1 if some are untouched by the bfs
        for (int r = 0; r < M; r++) {
            for (int c = 0; c < N; c++) {
                if (grid[r][c] == 1) {
                    return -1;
                }
            }
        }

        return latestTime;
    }
};
