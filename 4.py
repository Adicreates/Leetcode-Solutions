class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = [x for n in (nums1,nums2) for x in n]
        num.sort()
        print(num)
        n = len(num)
        if(n % 2 != 0):
            median = int(n/2)
            return float('%.5f' % num[median])
        else:
            mid1 = int(n/2) - 1
            mid2 = int(n/2)
            median = (num[mid1] + num[mid2]) / 2
            return float('%.5f' % median)
