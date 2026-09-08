class Solution {
public:
    void solve(vector<vector<char>>& board) {
        // idea: bfs from every "O island" to try and reach the edge
        // keep track of the cells that are part of the island,
        // fill them with X if never reach edge
        // else mark island as globally seen (no need to bfs it again)

        int M = board.size();
        int N = board[0].size();

        const vector<pair<int, int>> deltas = {
            {1, 0},
            {0, 1},
            {-1, 0},
            {0, -1}
        };

        vector<vector<bool>> globalSeen(M, vector<bool>(N, false));

        auto bfs = [&](int startRow, int startCol) {
            vector<pair<int, int>> thisIsland;
            queue<pair<int, int>> frontier;
            frontier.push({startRow, startCol});
            bool surrounded = true;
            while (!frontier.empty()) {
                auto [row, col] = frontier.front();
                frontier.pop();
                if (row < 0 || row >= M ||
                    col < 0 || col >= N || 
                    board[row][col] != 'O' ||
                    globalSeen[row][col]
                ) {
                    continue;
                }
                if (row <= 0 || row >= M - 1 || col <= 0 || col >= N - 1) {
                    surrounded = false;
                }
                thisIsland.push_back({row, col});
                globalSeen[row][col] = true;

                for (auto [drow, dcol] : deltas) {
                    int nrow = row + drow;
                    int ncol = col + dcol;
                    frontier.push({nrow, ncol});
                }
            }
            if (!surrounded)
                return;
            for (auto [row, col] : thisIsland) {
                board[row][col] = 'X';
            }
        };

        for (int row = 0; row < M; row++) {
            for (int col = 0; col < N; col++) {
                if (board[row][col] == 'O' && !globalSeen[row][col]) {
                    bfs(row, col);
                }
            }
        }
    }
};
