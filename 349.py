class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1 = []
        for i in nums1:
            if i in nums2:
                list1.append(i)
                nums2.remove(i)
        list1 = list(set(list1))
        return list1
