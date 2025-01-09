from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def getNext(idx: int) -> int:
            return (idx + nums[idx]) % n
        n = len(nums)
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = True
            cur_set = set()
            cur_idx = i
            while True:
                if cur_idx in cur_set:
                    if cur_idx == i and len(cur_set) > 1:
                        return True
                    else:
                        break
                if nums[cur_idx] * nums[i] <= 0:
                    break
                visited[cur_idx] = True
                cur_set.add(cur_idx)
                cur_idx = getNext(cur_idx)
        return False

if __name__ == "__main__":
    nums = [1,1,2]
    print(Solution().circularArrayLoop(nums))
