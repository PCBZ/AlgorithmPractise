class Solution:
    def countAndSay(self, n: int) -> str:
        def nextRLE(s: str) -> str:
            res = ''
            prev = ''
            count = 0
            for idx, ch in enumerate(s):
                if ch == prev or not prev:
                    count += 1
                else:
                    res += str(count) + prev
                    count = 1
                prev = ch
            res += str(count) + prev
            return res

        res = '1'
        if n == 1:
            return res
        for i in range(1, n):
            res = nextRLE(res)
        return res

if __name__ == '__main__':
    n = 4
    solution = Solution()
    print(solution.countAndSay(n))