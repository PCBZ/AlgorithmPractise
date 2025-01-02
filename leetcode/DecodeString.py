class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        num = 0
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
                if not s[i+1].isdigit():
                    stack.append(num)
            elif char == '[':
                stack.append(char)
            elif char in 'abcdefghijklmnopqrstuvwxyz' and stack:
                stack.append(char)
            elif char == ']':
                word = ""
                while stack[-1] != '[':
                    word = stack.pop() + word
                stack.pop()
                count = stack.pop()
                cur_word = count * word
                if stack:
                    stack.append(cur_word)
                else:
                    res += cur_word
            else:
                res += char
        return res


if __name__ == "__main__":
    s = "100[a]"
    print(Solution().decodeString(s))