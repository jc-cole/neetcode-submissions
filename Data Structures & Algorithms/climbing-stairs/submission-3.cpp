class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        vector<long long> waysToTop(n, 0);
        waysToTop[0] = 1;
        waysToTop[1] = 2;
        for (int i = 2; i < n; i++) {
            waysToTop[i] = waysToTop[i - 1] + waysToTop[i - 2];
        }
        return waysToTop[n - 1];
    }
};
