class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        flag = [True] * n
        flag[0] = flag[1] = False

        for i in range(2, int(math.ceil(math.sqrt(n)))):
            if(flag[i]):
                for j in range(i * i, n, i):
                    flag[j] = False
        return sum(flag)
