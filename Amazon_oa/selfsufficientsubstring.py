from collections import Counter

class Solution:
    def longestSelfsufficient(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for start in range(n):
            for end in range(start + 1, n):
                if start == 0 and end == n:
                    continue
                innerSet = set(s[start:end])
                outerSet = set(s[:start] + s[end:])
                if not innerSet & outerSet:
                    max_len = max(max_len, end - start)
        return max_len

if __name__ == "__main__":
    s = "amazonservices"
    print(Solution().longestSelfsufficient(s))
            