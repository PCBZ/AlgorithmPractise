from typing import List
from collections import defaultdict
from bisect import bisect_left

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            count += 1
        return count

if __name__ == "__main__":
    people = [1,5,3,5]
    limit = 7
    print(Solution().numRescueBoats(people, limit))