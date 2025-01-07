from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start = 0
        m, n = len(s), len(p)
        counter_p = Counter(p)
        counter = Counter(s[:n])
        res = []
        if counter == counter_p:
            res.append(0)
        for start in range(1, m - n + 1):
            print(s[start:start + n])
            counter[s[start - 1]] -= 1
            if counter[s[start - 1]] == 0:
                del counter[s[start - 1]]
            counter[s[start + n - 1]] += 1
            print(counter)
            if s[start + n - 1] not in p:
                continue
            if counter == counter_p:
                res.append(start)
        return res


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s, p))