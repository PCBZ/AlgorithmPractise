from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(num: int):
            if num > n:
                return
            res.append(num)
            for i in range(10):
                next_num = num * 10 + i
                if next_num > n:
                    break
                dfs(next_num)
        res = []
        for i in range(1, 10):
            dfs(i)
        return res
    
if __name__ == "__main__":
    print(Solution().lexicalOrder(13))