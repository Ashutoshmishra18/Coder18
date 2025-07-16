class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        i=len(nums)
        if i==2:
            return 2
        a=nums[0]&1
        gen=[1-a,a,1]
        for h in nums[1:]:
            g=h&1
            gen[g&1]+=1
            if g!=a:
                gen[2]+=1
                a=1-a
        return max(gen)


        