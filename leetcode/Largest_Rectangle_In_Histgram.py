from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights.append(0)
        for idx, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                calculate_height = heights[stack.pop()]
                width = idx - stack[-1] - 1 if stack else idx
                max_area = max(max_area, calculate_height * width)
            stack.append(idx)
        return max_area



if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    print(Solution().largestRectangleArea(heights))
    # Output: 10