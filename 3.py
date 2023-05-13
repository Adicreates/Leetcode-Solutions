class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) <= 1):
            return len(s)
        seen = {}
        l = 0
        r = 0
        longest = 0
        while(l < len(s) and r < len(s)):
            cur = s[r]
            if(cur in seen):
                prev = seen[cur]
                l = max(l, prev + 1)
            seen[cur] = r
            longest = max(longest, r - l + 1)
            r += 1
        return longest
