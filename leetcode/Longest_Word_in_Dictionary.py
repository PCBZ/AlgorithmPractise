from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = lambda x: (len(x), x))
        word_set = set()
        max_len = 0
        candidate = ""
        for word in words:
            if len(word) == 1:
                word_set.add(word)
            elif word[:-2] in word_set:
                word_set.add(word)
                print(word)
                if len(word) > max_len:
                    candidate = word
                    max_len = len(word)
        return candidate

if __name__ == "__main__":
    words = ["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]
    print(Solution().longestWord(words))