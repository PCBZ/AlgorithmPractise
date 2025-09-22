"""
LeetCode #842: Split Array into Fibonacci Sequence
https://leetcode.com/problems/split-array-into-fibonacci-sequence/

Split string of digits into Fibonacci-like sequence using backtracking.
Time: O(10^N), Space: O(N)
"""

from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        """Split string into Fibonacci sequence using backtracking."""
        n = len(num)
        
        def backtrack(index: int, path: List[int]) -> List[int]:
            """Build Fibonacci sequence from current position."""
            # Base case: reached end with valid sequence
            if index == len(num) and len(path) >= 3:
                return path
                
            num_int = 0
            # Try all possible numbers from current index
            for i in range(index, n):
                # Handle leading zeros
                if num[index] == "0" and i != index:
                    break
                    
                num_int = num_int * 10 + int(num[i])
                
                # Check Fibonacci property if we have 2+ numbers
                if len(path) >= 2:
                    expected_sum = path[-2] + path[-1]
                    if num_int < expected_sum:
                        continue  # Too small, try longer
                    elif num_int > expected_sum:
                        break  # Too large, stop here
                
                # Try this number and continue
                res = backtrack(i + 1, path + [num_int])
                if res:
                    return res
                    
            return []
        
        return backtrack(0, [])


if __name__ == "__main__":
    test_cases = ["123456579", "11235813", "112358130", "0123", "1101111"]
    sol = Solution()
    
    for num in test_cases:
        result = sol.splitIntoFibonacci(num)
        print(f"'{num}' -> {result}")
