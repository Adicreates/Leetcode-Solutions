class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum1 = 0
        for i in range(len(accounts)):
            sum2 = sum(accounts[i])
            sum1 = max(sum1, sum2)
        return sum1
