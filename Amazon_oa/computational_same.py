from typing import List
from collections import defaultdict

class Solution:
    def computational_same(self, processes: List[int], m: int) -> int:
        processes.sort()
        n = len(processes)
        count = 0
        left, right = 0, 0
        for left in range(n):
            while right < n and processes[right] - processes[left] <= m:
                right += 1
            count += right - 1 - left
            left += 1
            right = left
        return count

if __name__ == "__main__":
    processess = [7, 10, 13, 11]
    m = 3
    print(Solution().computational_same(processess, m))