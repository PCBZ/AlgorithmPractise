from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        next_greater = {}
        stack = []
        for num in nums2:
            if not stack or stack[-1] >= num:
                stack.append(num)
            else:
                while stack and stack[-1] < num:
                    ele = stack.pop()
                    next_greater[ele] = num
                stack.append(num)
        for idx, num in enumerate(nums1):
            if num in next_greater:
                res[idx] = next_greater[num]
        return res
    
if __name__ == "__main__":
    nums1, nums2 = [2, 4], [1, 2, 3, 4]
    print(Solution().nextGreaterElement(nums1, nums2))