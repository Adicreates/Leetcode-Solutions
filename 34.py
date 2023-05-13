class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(target not in nums):
            return [-1,-1]
        i = 0
        while(i < len(nums)):
            if(target == nums[i]):
                final = max(index for index, item in enumerate(nums) if item == target)
                return [i, final]
            else:
                i += 1
