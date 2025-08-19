from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left_less, right_less = [None] * n, [None] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left_less[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right_less[i] = stack[-1] if stack else n
            stack.append(i)
        
        MOD = 10**9 + 7
        res = 0
        for i in range(n):
            res = (res + arr[i] * (i - left_less[i]) * (right_less[i] - i)) % MOD
        return res


if __name__ == "__main__":
    arr = [3, 1, 2, 4]
    print(Solution().sumSubarrayMins(arr))  # Example usage