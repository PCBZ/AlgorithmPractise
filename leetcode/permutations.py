class Solution:
    def permute(self, nums):
        n = len(nums)
        def backtrack(path):
            if len(path) == n:
                res.append(path[:])
            for i in range(n):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
        res = []
        backtrack([])
        return res

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().permute(nums))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]