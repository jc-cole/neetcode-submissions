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
                    0 <= y + dy && y + dy < N
                ) {
                    frontier.push({x + dx, y + dy, dist + 1});
                }
            }
        };

        auto bfs = [&](int startX, int startY) {
            queue<tuple<int, int, int>> frontier;
            enqueueNeighbors(startX, startY, frontier, 0);
            while (!frontier.empty()) {
                auto [x, y, dist] = frontier.front();
                frontier.pop();
                if (grid[x][y] <= dist)
                    continue;
                grid[x][y] = dist;
                enqueueNeighbors(x, y, frontier, dist);
            }
        };

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == 0) {
                    bfs(i, j);
                }
            }
        }
    }
};
