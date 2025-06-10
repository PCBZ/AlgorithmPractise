from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = end = 0
        n = len(s)
        counter = defaultdict(int)
        max_count = 0
        max_len = 0
        while end < n:
            while end < n and end - start - max_count <= k:
                counter[s[end]] += 1
                max_count = max(max_count, counter[s[end]])
                end += 1
            max_len = max(max_len, end - start - 1)  # corrected here
            counter[s[start]] -= 1
            start += 1
        return max_len

if __name__ == "__main__":
    s = "XYYX"
    k = 2
    print(Solution().characterReplacement(s, k))  # Output: 4

    s = "AAABABB"
    k = 1
    print(Solution().characterReplacement(s, k))  # Output: 5