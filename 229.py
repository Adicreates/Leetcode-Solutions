class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = {}
        for i in nums:
            m[i] = m.get(i, 0) + 1
        list1 = []
        for i in nums:
            if(m[i] > n // 3):
                list1.append(i)
        return set(list1)
