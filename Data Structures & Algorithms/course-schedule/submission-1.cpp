class Solution {
public:
    bool dfsFrom(int start, vector<int>& state, unordered_map<int, vector<int>>& adjList) {
        state[start] = 1;
        for (int prerequisite : adjList[start]) {

            if (state[prerequisite] == 1)
                return false;

            if (state[prerequisite] == 0 && !dfsFrom(prerequisite, state, adjList))
                return false;
        }

        state[start] = 2;
        return true;
    };
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // idea: this is equivalent to asking if there does not exist a cycle in the dg of courses
        
        vector<int> state(numCourses, false);
        // 0: unvisited
        // 1: currently on the DFS path
        // 2: completely processed

        unordered_map<int, vector<int>> adjList;
        for (vector<int> edge : prerequisites) {
            int course = edge[0];
            int prereq = edge[1];
            adjList[course].push_back(prereq);
        }

        for (int i = 0; i < numCourses; i++) {
            if (state[i] == 0 && !dfsFrom(i, state, adjList))
                return false;
        }

        return true;
    }
};
