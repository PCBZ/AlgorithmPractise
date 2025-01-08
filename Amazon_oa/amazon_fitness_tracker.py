from typing import List

class Solution:
    def findMaximumCalories(heights: List[int]) -> int:
        heights.sort()
        orders = []
        n = len(heights)
        left, right = 0, n - 1
        direction = False
        while left <= right:
            if direction:
                orders.append(heights[left])
                left += 1
            else:
                orders.append(heights[right])
                right -= 1
            direction = not direction
        prev = 0
        calorie = 0
        for i in range(n):
            calorie += (orders[i] - prev) ** 2
            prev = orders[i]
        return calorie



if __name__ == "__main__":
    heights = [5, 2, 5]
    print(Solution.findMaximumCalories(heights))