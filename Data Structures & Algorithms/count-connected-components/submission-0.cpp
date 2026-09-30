class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        // idea: while still unseen nodes, bfs that node
        // 1 bfs = 1 connected component

        vector<vector<int>> adjList(n);

        for (auto edge : edges) {
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }

        vector<bool> seen(n, false);

        int components = 0;

        for (int i = 0; i < n; i++) {
            if (!seen[i]) {

                queue<int> frontier;
                frontier.push(i);

                while (!frontier.empty()) {
                    int current = frontier.front();
                    frontier.pop();

                    seen[current] = true;

                    for (int neighbor : adjList[current]) {
                        if (!seen[neighbor]) {
                            frontier.push(neighbor);
                        }
                    }
                }

                components++;
            }
            
        }

        return components;

    }
};
