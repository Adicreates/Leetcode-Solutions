class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m = {}
        for i in nums:
            m[i] = m.get(i, 0) + 1
        
        for i in nums:
            if(m[i] > n // 2):
                return i
