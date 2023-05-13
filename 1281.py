class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = list(map(int, str(n)))
        prod = 1
        sum1 = 0
        for i in range(len(res)):
            prod *= res[i]
            sum1 += res[i]
        return prod - sum1
