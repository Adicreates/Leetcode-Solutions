class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        nums.sort()
        diff = 0
        for i in range(len(nums)):
            diff1 = nums[i] - nums[i-1]
            diff = max(diff, diff1)
        return diff
