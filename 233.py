class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        p = 1
        while p <= n:
            d = (n // p) % 10
            count += (n // (10 * p)) * p
            if d == 1:
                count += (n % p) + 1
            elif d > 1:
                count += p
            p *= 10
        return count 
