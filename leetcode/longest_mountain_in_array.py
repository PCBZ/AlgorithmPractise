from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        prev = arr[0]
        has_peak = False
        n = len(arr)
        largest = 0
        prev_acsd = 0
        cur_len = 1
        for i in range(1, n):
            if arr[i] > prev:
                if has_peak:
                    largest = max(largest, cur_len)
                    cur_len = 2
                    has_peak = False
                else:
                    cur_len += 1
                prev_acsd = 1
            elif arr[i] < prev:
                if has_peak:
                    cur_len += 1
                    largest = max(largest, cur_len)
                else:
                    if prev_acsd == 1:
                        has_peak = True
                        cur_len += 1
                        largest = max(largest, cur_len)
                    else:
                        cur_len = 1
                prev_acsd = -1
            else:
                cur_len = 1
                prev_acsd = 0
            prev = arr[i]
        return largest
    
if __name__ == "__main__":
    arr = [875,884,239,731,723,685]
    print(Solution().longestMountain(arr))