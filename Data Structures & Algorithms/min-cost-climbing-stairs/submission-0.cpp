class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {

        int N = cost.size();
        vector<int> DP(N, 0);

        DP[N - 1] = cost[N - 1];
        DP[N - 2] = cost[N - 2];

        for (int i = N - 3; i >= 0; i--) {
            DP[i] = cost[i] + min(DP[i + 1], DP[i + 2]);
        }

        return min(DP[0], DP[1]);
    }
};
