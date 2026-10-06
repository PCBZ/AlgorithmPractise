import bisect

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) > 1:
            fi, se = stones.pop(0), stones.pop(0)
            print(fi, se)
            if fi != se:
                remain = abs(fi - se)
                bisect.bisect_left(stones, remain)
            print(stones)
        return stones[0] if stones else 0

print(Solution().lastStoneWeight([2,7,4,1,8,1]))  # Output: 1