from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s: str) -> bool:
            return s == s[::-1]
        n = len(s)
        def backTrace(s: str, start: int, path: List[str]):
            if start == n:
                res.append(path[:])
            for end in range(start+1, n+1):
                substr = s[start:end]
                if isPalindrome(substr):
                    path.append(substr)
                    backTrace(s, end, path)
                    path.pop()
        res = []
        backTrace(s, 0, [])
        return res
            
s = "aab"
print(Solution().partition(s))

