class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        move_count = 0
        while left != right:
            left >>= 1
            right >>= 1
            move_count += 1
        return left << move_count


left, right = 5, 7
print(Solution().rangeBitwiseAnd(left, right))