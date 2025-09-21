"""
LeetCode #957: Prison Cells After N Days
https://leetcode.com/problems/prison-cells-after-n-days/

Algorithm: Use cycle detection to handle large N values efficiently.
Time Complexity: O(min(N, 2^8)), Space Complexity: O(2^8)
"""

from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        """Return prison cell states after N days using cycle detection."""
        def get_nextday(cells: List[int]) -> List[int]:
            """Calculate next day's cell states."""
            n = len(cells)
            new_cells = [0] * n
            for i in range(1, n-1):
                new_cells[i] = 1 if cells[i-1] == cells[i+1] else 0
            return new_cells

        seen = {}
        day = 0
        
        while day < n:
            state = tuple(cells)
            
            if state in seen:
                cycle_len = day - seen[state]
                n = day + (n - day) % cycle_len
            else:
                seen[state] = day
                
            if day < n:
                day += 1
                cells = get_nextday(cells)
                
        return cells


if __name__ == "__main__":
    # Quick test
    test_cells = [1,0,0,1,0,0,1,0]
    n = 1000000000
    result = Solution().prisonAfterNDays(test_cells, n)
    print(f"Quick test result: {result}")