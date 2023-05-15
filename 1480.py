class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = []
        sum1 = 0
        for i in range(len(nums)):
            sum1 += nums[i]
            sum.append(sum1)
        return (sum)
