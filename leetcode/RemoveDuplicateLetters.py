from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set()
        counter = Counter(s)
        for char in s:
            counter[char] -= 1
            if char in visited:
                continue
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                rm_char = stack.pop()
                visited.remove(rm_char)
            stack.append(char)
            visited.add(char)
        return ''.join(stack)

if __name__ == "__main__":
    s = "cbacdcbc"
    print(Solution().removeDuplicateLetters(s))