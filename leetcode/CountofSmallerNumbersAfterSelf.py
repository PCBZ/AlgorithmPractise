from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        def insert(num: int, small_count: int, root: TreeNode) -> int:
            if num <= root.val:
                if not root.left:
                    root.left = TreeNode(num)
                    return small_count
                return insert(num, small_count, root.left)
            else:
                if not root.right:
                    root.right = TreeNode(num)
                    return small_count+1
                return insert(num, small_count+1, root.right)

        counts = [0]
        root = TreeNode(nums[-1])
        n = len(nums)
        for i in range(n-2, -1, -1):
            counts.insert(0, insert(nums[i], 0, root))
        return counts


class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

if __name__ == "__main__":
    nums = [2, 0, 1]
    print(Solution().countSmaller(nums))