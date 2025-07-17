class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        n=len(nums)
        dp=[defaultdict(int) for i in range(n)]
        max_len=1
        for a in range(n):
            for b in range(a):
                mod=(nums[a]+nums[b])%k
                dp[a][mod] = max(dp[a][mod], dp[b].get(mod, 1) + 1)
                max_len = max(max_len, dp[a][mod])
        return max_len
        