class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if(len(arr) <= 2):
            return True

        arr.sort()
        diff = abs(arr[1] - arr[0])
        for i in range(len(arr)-1, 1, -1):
            if(abs(arr[i] - arr[i-1]) != diff):
                    return False
        return True
