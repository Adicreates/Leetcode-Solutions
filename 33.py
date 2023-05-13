class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        while(i < len(nums)):
            if(target == nums[i]):
                return i
            else:
                i += 1
        return -1
