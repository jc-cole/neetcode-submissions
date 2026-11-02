class Solution {
public:
    int rob(vector<int>& nums) {

        if (nums.size() == 1) {
            return nums[0];
        } else if (nums.size() == 2) {
            return max(nums[0], nums[1]);
        } else if (nums.size() == 3) {
            return max(nums[0] + nums[2], nums[1]);
        }

        vector<int> DP(nums.size(), 0);
        DP[0] = nums[0];
        DP[1] = nums[1];
        DP[2] = DP[0] + nums[2];

        for (int i = 3; i < nums.size(); i++) {
            DP[i] = nums[i] + max(DP[i-2], DP[i-3]);
        }

        return max(DP[nums.size() - 1], DP[nums.size() - 2]);

    }
};
