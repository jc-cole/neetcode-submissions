class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        
        int M = grid.size();
        int N = grid[0].size();

        vector<pair<int, int>> deltas = {
            {1, 0},
            {0, 1},
            {-1, 0},
            {0, -1}
        };

        auto enqueueNeighbors = [&](int x, int y, queue<tuple<int, int, int>>& frontier, int dist) {
            for (auto [dx, dy] : deltas) {
                if (
                    0 <= x + dx && x + dx < M &&
                    0 <= y + dy && y + dy < N &&
                    grid[x + dx][y + dy] > dist + 1
                ) {
                    grid[x + dx][y + dy] = dist + 1;
                    frontier.push({x + dx, y + dy, dist + 1});
                }
            }
        };

        queue<tuple<int, int, int>> frontier;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == 0) {
                    frontier.push({i, j, 0});
                }
            }
        }
        while (!frontier.empty()) {
            auto [x, y, dist] = frontier.front();
            frontier.pop();
            enqueueNeighbors(x, y, frontier, dist);
        }
    }
};
