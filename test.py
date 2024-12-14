from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        lengths = {}  # Dictionary to store the lengths of sequences
        max_length = 0

        for num in nums:
            if num not in lengths:  # If the number is not already processed
                # Get the lengths of the left and right sequences
                left = lengths.get(num - 1, 0)
                right = lengths.get(num + 1, 0)

                # Total sequence length
                current_length = left + 1 + right
                max_length = max(max_length, current_length)

                # Update the boundaries of the sequence
                lengths[num] = current_length
                lengths[num - left] = current_length
                lengths[num + right] = current_length

        return max_length
    
nums = [100,4,200,1,3,2]
print(Solution().longestConsecutive(nums))