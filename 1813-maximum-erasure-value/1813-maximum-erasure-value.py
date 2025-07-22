class Solution:
    def maximumUniqueSubarray(self, nums):
        let= 0
        ram = 0
        nam = len(nums)
        frequency = {}
        total = 0
        max_sum = 0

        while ram < nam:
            frequency[nums[ram]] = frequency.get(nums[ram], 0) + 1
            total += nums[ram]

            while (ram - let + 1) > len(frequency):
                frequency[nums[let]] -= 1
                total -= nums[let]
                if frequency[nums[let]] == 0:
                    del frequency[nums[let]]
                let += 1

            max_sum = max(max_sum, total)
            ram += 1

        return max_sum