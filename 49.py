class Solution:
    def findHash(self, s):
            return ''.join(sorted(s))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # all words are same when sorted => same anagram
        list1 = []
        m = {}

        for s in strs:
            hashed = self.findHash(s)
            if(hashed not in m):
                m[hashed] = []
            m[hashed].append(s)

        for i in m.values():
            list1.append(i)
        return list1
