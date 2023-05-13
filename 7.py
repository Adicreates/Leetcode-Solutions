class Solution:
    def reverse(self, x: int) -> int:
        n = 0
        temp = x
        x = abs(x)
        while(x > 0):
            new = x % 10
            n = n * 10 + new
            x = x // 10
        if(n > 2**31):
            return 0
        elif(temp < 0):
            return -n
        return n
