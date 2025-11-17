from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        for i in range(n, 0, -1):
            max_idx = max(range(i), key=lambda x: arr[x])
            if max_idx == i:
                continue
            if max_idx != 0:
                arr = arr[:max_idx+1][::-1] + arr[max_idx+1:]
                ans.append(max_idx + 1)
            if i != 1:
                arr = arr[:i][::-1] + arr[i:]
                ans.append(i)
        return ans

if __name__ == "__main__":
    test_arr = [3, 2, 4, 1]
    print(Solution().pancakeSort(test_arr))