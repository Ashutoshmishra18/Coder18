import java.util.*;

class Solution {
    public int maximumLength(int[] nums, int k) {
        int n = nums.length;
        int maxLen = 1;
        Map<Integer, Integer>[] dp = new HashMap[n];
        for (int i = 0; i < n; i++) {
            dp[i] = new HashMap<>();
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int mod = (nums[j] + nums[i]) % k;
                int prevLen = dp[j].getOrDefault(mod, 1);
                dp[i].put(mod, Math.max(dp[i].getOrDefault(mod, 0), prevLen + 1));
                maxLen = Math.max(maxLen, dp[i].get(mod));
            }
        }

        return maxLen;
    }

}
