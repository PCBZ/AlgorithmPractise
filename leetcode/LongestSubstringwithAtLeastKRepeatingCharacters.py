from collections import defaultdict

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def helper(start: int, end: int) -> int:
            if end - start < k:
                return 0
            freq = defaultdict(int)
            for i in range(start, end):
                freq[s[i]] += 1
            for i in range(start, end):
                if freq[s[i]] < k:
                    left = helper(start, i)
                    right = helper(i + 1, end)
                    return max(left, right)
            return end - start
        return helper(0, len(s))

if __name__ == "__main__":
    s = "ababbc"
    k = 2
    print(Solution().longestSubstring(s, 2))