class Solution {
public:

    bool dfs(int node, vector<vector<int>>& adjList, vector<int>& state, int myParent) {
        state[node] = 1;

        for (int neighbor : adjList[node]) {
            if (neighbor == myParent)
                continue;

            if (state[neighbor] == 0 && !dfs(neighbor, adjList, state, node))
            return false;

            if (state[neighbor] == 1)
                return false;
        }
        state[node] = 2;
        return true;
    }


    bool validTree(int n, vector<vector<int>>& edges) {
        
        vector<vector<int>> adjList(n);

        for (auto edge : edges) {
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }

        vector<int> state(n, 0);

        if (!dfs(0, adjList, state, -1))
            return false; // cycle
        
        for (int i = 0; i < n; i++) {
            if (state[i] == 0) {
                return false; // not connected
            }
        }

        return true;
    }
};
