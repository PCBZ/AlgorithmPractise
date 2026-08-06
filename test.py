from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_counter = Counter(t)
        counter = Counter()

        start = 0
        min_window = float('inf')
        res = ""

        for end, char in enumerate(s):
            counter[char] += 1
            while start < end and (s[start] not in target_counter or counter[s[start]] > target_counter[s[start]]):
                counter[s[start]] -= 1
                if counter[s[start]] == 0:
                    del counter[s[start]]
                start += 1
                if len(counter) < min_window:
                    min_window = len(counter)
                    res = s[start:end+1]
        return res
    
s = "ADOBECODEBANC"
t = "ABC"
solution = Solution()
print(solution.minWindow(s, t))