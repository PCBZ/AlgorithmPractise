from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        t = sorted(nums)
        n = len(nums)
        i, j = (n - 1) // 2, n - 1
        trans = True
        for k in range(n):
            if trans:
                nums[k] = t[i]
                i -= 1
            else:
                nums[k] = t[j]
                j -= 1
            trans = not trans 

if __name__ == "__main__":
    nums = [4,5,5,6]
    Solution().wiggleSort(nums)
    print(nums)
    