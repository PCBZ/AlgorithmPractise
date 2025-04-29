from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def isExpressive(s: str, word: str) -> bool:
            n1, n2 = len(s), len(word)
            p1 = p2 = 0
            while p1 < n1 and p2 < n2:
                if s[p1] != word[p2]:
                    return False
                p1_count = 1
                while p1 + 1 < n1 and s[p1 + 1] == s[p1]:
                    p1 += 1
                    p1_count += 1
                p2_count = 1
                while p2 + 1 < n2 and word[p2 + 1] == word[p2]:
                    p2 += 1
                    p2_count += 1
                if p1_count - p2_count < 2 and p1_count != p2_count:
                    return False
                p1 += 1
                p2 += 1
            return p1 == n1 and p2 == n2
        
        return sum(1 for word in words if isExpressive(s, word))
    

if __name__ == "__main__":
    s = "heeellooo"
    words = ["hello", "hi", "helo"]
    print(Solution().expressiveWords(s, words))