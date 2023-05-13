class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum = 0
        for i in range(len(operations)):
            if(operations[i].startswith('++') or operations[i].endswith('++')):
                sum += 1
            else:
                sum -= 1
        return sum
