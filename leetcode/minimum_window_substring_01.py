from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        left = right = 0
        start, length = 0, float("inf")
        valid_count = 0
        window = {}
        while right < len(s):
            char = s[right]
            right += 1
            if char in need:
                window[char] = window.get(char, 0) + 1
                if window[char] == need[char]:
                    valid_count += 1
            
            while valid_count == len(need):
                if right - left < length:
                    start, length = left, right - left
                char = s[left]
                left += 1
                if char in need:
                    if window[char] == need[char]:
                        valid_count -= 1
                    window[char] -= 1
        
        return "" if length == float("inf") else s[start:start+length]

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))  # Output: "BANC"