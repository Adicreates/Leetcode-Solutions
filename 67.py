class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binary = int(a, 2) + int(b, 2)
        sum1 = bin(binary)
        return sum1[2:]
