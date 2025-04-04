from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def isConcatenated(word: str) -> bool:
            n = len(word)
            cur_word_set = set(filter(lambda w: w != word, word_set))

            def dfs(start: int) -> bool:
                if start == n:
                    return True
                exist = False
                for i in range(start, n):
                    if word[start:i+1] in cur_word_set:
                        print(word[start:i+1], word)
                        exist = exist or dfs(i + 1)
                return exist
            return dfs(0)
        
        word_set = set(words)
        return list(filter(isConcatenated, words))

        
if __name__ == "__main__":
    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    print(Solution().findAllConcatenatedWordsInADict(words))