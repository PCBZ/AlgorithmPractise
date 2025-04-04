from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        queue = deque([(beginWord, 1)])
        while queue:
            cur_word, level = queue.popleft()
            for i, char in enumerate(cur_word):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    next_word = cur_word[:i] + char + cur_word[i+1:]
                    if next_word == endWord:
                        return level + 1
                    if next_word in word_set:
                        queue.append((next_word, level + 1))
                        word_set.remove(next_word)
        
        return 0


if __name__ == "__main__":
    print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))