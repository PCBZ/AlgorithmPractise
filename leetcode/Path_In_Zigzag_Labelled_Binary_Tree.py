import math

class Solution:
    def pathInZigZagTree(self, label: int) -> list[int]:
        acc, increment = 0, 1
        while acc + increment < label:
            acc += increment
            increment *= 2
        
        res = [label]
        cur_label = label
        while cur_label != 1:
            increment //= 2
            line_count = math.ceil((cur_label - acc) / 2) if cur_label != acc else increment
            cur_label = acc - line_count + (1 if cur_label != acc else 0)
            res.insert(0, cur_label)
            acc -= increment
        
        return res

print(Solution().pathInZigZagTree(3))  # Output: [1, 3, 4, 14]