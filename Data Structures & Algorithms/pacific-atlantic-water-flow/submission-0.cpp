class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int M = heights.size();
        int N = heights[0].size();

        const vector<pair<int, int>> directions = {
            {1, 0},
            {0, 1},
            {-1, 0},
            {0, -1}
        };

        auto bfs = [&](int startRow, int startCol) {
            queue<pair<int, int>> frontier;
            vector<vector<int>> seen(M, vector<int>(N, false));
            seen[startRow][startCol] = true;
            frontier.push({startRow, startCol});
            bool pacific = false;
            bool atlantic = false;
            
            while (!frontier.empty()) {
                auto [row, col] = frontier.front();
                frontier.pop();
                for (auto [drow, dcol] : directions) {
                    int nrow = row + drow;
                    int ncol = col + dcol;
                    if (
                        0 <= nrow && nrow < M &&
                        0 <= ncol && ncol < N &&
                        !seen[nrow][ncol] &&
                        heights[row][col] >= heights[nrow][ncol]
                    ) {
                        seen[nrow][ncol] = true;
                        frontier.push({nrow, ncol});
                    } else if (nrow < 0 || ncol < 0) {
                        pacific = true;
                    } else if (nrow >= M || ncol >= N) {
                        atlantic = true;
                    }
                }
            }
            return pacific && atlantic;
        };
        vector<vector<int>> res;
        for (int r = 0; r < M; r++) {
            for (int c = 0; c < N; c++) {
                if (bfs(r, c)) {
                    res.push_back({r, c});
                }
            }
        }
        return res;
    }
};
