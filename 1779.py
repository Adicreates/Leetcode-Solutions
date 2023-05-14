class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid=[]
        list1 = []
        for i in points:
            if i[0]==x or i[1]==y:
                valid.append(i)
        if len(valid) == 0:
            return -1
        else:
            for i in valid:
                list1.append(abs(x - i[0]) + abs(y - i[1]))
            if valid[list1.index(min(list1))] in valid:
                return points.index(valid[list1.index(min(list1))])
        
            
            
            
            

            
