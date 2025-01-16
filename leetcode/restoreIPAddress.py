from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        def traceBack(start: int, ips: List[str]):
            if start == n and len(ips) == 4:
                res.append('.'.join(ips))
                return
            if len(ips) == 4:
                return
            for i in range(3):
                 if start+i+1 <= n and int(s[start:start+i+1]) <= 255:
                    ips.append(s[start:start+i+1])
                    traceBack(start+i+1, ips)
                    ips.pop()
        res = []
        traceBack(0, [])
        return res
        

if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))