class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        n1, n2 = a, b
        res = []
        while n1 > 0 and n2 > 0:
            if n1 > n2:
                if not res:
                    res.append('aa')
                    n1 -= 2
                else:
                    if res[-1][-1] == 'a':
                        res.append('b')
                        n2 -= 1
                    else:
                        res.append('aa')
                        n1 -= 2
            elif n1 == n2:
                if not res:
                    res.append('a')
                    n1 -= 1
                else:
                    if res[-1][-1] == 'a':
                        res.append('b')
                        n2 -= 1
                    else:
                        res.append('a')
                        n1 -= 1
            else:
                if not res:
                    res.append('bb')
                    n2 -= 2
                else:
                    if res[-1][-1] == 'a':
                        res.append('bb')
                        n2 -= 2
                    else:
                        res.append('a')
                        n1 -= 1
        
        res.append("a" * n1 + "b" * n2)
        
        return ''.join(res)
    
if __name__ == "__main__":
    print(Solution().strWithout3a3b(1, 4))