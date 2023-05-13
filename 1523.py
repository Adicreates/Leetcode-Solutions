class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = (high - low) // 2
        if(low % 2 == 0 and high % 2 == 0):
            return n
        else:
            return n + 1
