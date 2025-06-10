from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(index: int) -> bool:
            counter[s[index]] -= 1
            is_match = counter == pattern
            counter[s[index]] += 1
            return is_match

        set_t = set(t)
        pattern = Counter(t)
        counter = Counter()
        n = len(s)
        shortest = float('inf')
        res = ""
        start = 0
        for end in range(n):
            if s[end] in set_t:
                counter[s[end]] += 1
            while counter == pattern:
                counter[s[start]] -= 1
                start += 1
                if end - start + 1 < shortest:
                    res = s[start:end+1]
                    shortest = end - start + 1
        return res

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))  # Output: "BANC"