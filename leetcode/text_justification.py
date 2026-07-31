from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, line_len = [], 0
        for word in words:
            if len(line) + line_len + len(word) > maxWidth:
                space_count = 