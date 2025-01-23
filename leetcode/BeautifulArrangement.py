from typing import List

class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        def backTrack(path: List[int]):
            nonlocal count
            if len(path) == n:
                count += 1
            for i in range(1, n + 1):
                if i 
                    idx = len(path) + 1
                    if i % idx == 0 or idx % i == 0:
                        path.append(i)
                        backTrack(path)
                        path.pop()
        backTrack([])
        return count


if __name__ == "__main__":
    n = 4
    print(Solution().countArrangement(n))