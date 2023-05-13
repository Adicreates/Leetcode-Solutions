class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in range(0, len(nums)):
            sum = sum + nums[i]
        
        n = len(nums)
        new_sum = n * (n + 1) / 2
        return int(new_sum - sum)
