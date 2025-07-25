class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_sum=max(nums)
        if max_sum<=0: return max_sum
        seen, Sum=0, 0
        for x in nums:
            if x>=0 and (seen>>x)&1==0:
                Sum+=x
                seen|=(1<<x)
        return Sum

        