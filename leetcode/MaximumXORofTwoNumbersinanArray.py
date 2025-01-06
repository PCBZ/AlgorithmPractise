from typing import List

class Trie:
    def __init__(self):
        self.left = None
        self.right = None

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Trie()

        def add(num: int):
            node = root
            for i in range(30, -1, -1):
                digit = (num >> i) & 1
                if digit == 0:
                    if not node.left:
                        node.left = Trie()
                    node = node.left
                else:
                    if not node.right:
                        node.right = Trie()
                    node = node.right
        
        def check(num: int) -> int:
            node = root
            ret = 0
            for i in range(30, -1, -1):
                digit = (num >> i) & 1
                if digit == 0:
                    if node.right:
                        node = node.right
                        ret = (ret << 1) + 1
                    else:
                        node = node.left
                        ret = (ret << 1)
                else:
                    if node.left:
                        node = node.left
                        ret = (ret << 1) + 1
                    else:
                        node = node.right
                        ret = (ret << 1)
            return ret
        
        n = len(nums)
        res = 0
        for i in range(n):
            add(nums[i-1])
            res = max(res, check(nums[i]))
        return res

if __name__ == "__main__":
    nums = [3,10,5,25,2,8]
    print(Solution().findMaximumXOR(nums))