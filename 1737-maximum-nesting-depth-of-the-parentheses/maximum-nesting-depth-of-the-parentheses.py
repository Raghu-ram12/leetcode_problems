class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        n = len(s)
        maxi = 0
        
        for i in range(n):
            if s[i] == '(':
                cnt += 1
            if s[i] == ')':
                cnt -= 1
            maxi = max(maxi, cnt)
        return maxi