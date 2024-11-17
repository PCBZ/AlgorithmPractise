from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        left, right = 0, len(words) * word_len - 1
        res = []
        while right < len(s):
            words_list = words.copy()
            i = left
            while i <= right - word_len + 1:
                word = s[i:i + word_len]
                if word in words:
                    words_list.remove(word)
                else:
                    break
                i += word_len
            if not words_list:
                res.append(left)
            left += 1
            right += 1
        return res

if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    solution = Solution()
    print(solution.findSubstring(s, words))