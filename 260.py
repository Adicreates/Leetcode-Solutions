class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        list1 = []
        for i in nums:
            if nums.count(i) == 1:
                list1.append(i)
        return list1
