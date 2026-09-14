class Solution {
public:
    bool dfs(int node, vector<int>& state, unordered_map<int, vector<int>>& adjList, vector<int>& result) {
        state[node] = 1;
        for (int neighbor : adjList[node]) {
            if (state[neighbor] == 1) {
                return false;
            }

            if (state[neighbor] == 0 && !dfs(neighbor, state, adjList, result)) {
                return false;
            }
        }
        state[node] = 2;
        result.push_back(node);
        return true;
    }

    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {

        vector<int> state(numCourses, 0);
        unordered_map<int, vector<int>> adjList;

        for (auto prereq : prerequisites) {
            int course = prereq[0];
            int hasPrereq = prereq[1];
            adjList[course].push_back(hasPrereq);
        }
        vector<int> result;
        for (int i = 0; i < numCourses; i++) {
            if (state[i] == 0 && !dfs(i, state, adjList, result))
                return {};
        }

        return result;

    }
};
