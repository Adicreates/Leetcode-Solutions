class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True) 
        for i in range(len(nums) - 2): 
            if(nums[i+1] + nums[i+2] > nums[i]): # 10,2,1,1
                return nums[i] + nums[i+1] + nums[i+2]
        return 0

        
