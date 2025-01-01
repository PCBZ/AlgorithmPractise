from typing import List
import random

class Solution:
    def shuffle(self, arr: List[int]):
        for i in range(len(arr) - 1, 0, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Solution().shuffle(nums)
    print(nums)