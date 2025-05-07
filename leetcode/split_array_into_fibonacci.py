from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)
        def backtrack(index: int, path: List[int]) -> List[int]:
            if index == len(num) and len(path) >= 3:
                return path
            num_int = 0
            for i in range(index, n):
                if num[index] == "0" and i != index:
                    break
                num_int = num_int * 10 + int(num[i])
                if len(path) >= 2:
                    if num_int < path[-2] + path[-1]:
                        continue
                    elif num_int > path[-2] + path[-1]:
                        break
                res = backtrack(i + 1, path + [num_int])
                if res:
                    return res
            return []
        
        return backtrack(0, [])


if __name__ == "__main__":
    num = "123456579"
    print(Solution().splitIntoFibonacci(num))
    # num = "11235813"
    # print(Solution().splitIntoFibonacci(num))
    # num = "112358130"
    # print(Solution().splitIntoFibonacci(num))
    num = "0123"
    print(Solution().splitIntoFibonacci(num))
    num = "1101111"
    print(Solution().splitIntoFibonacci(num))
