def int2bin(t: int) -> str:
    res = []
    p = 1
    while t:
        k = t % pow(2, p)
        res.insert(0, str(k))
        t //= pow(2, p)
    return ''.join(res)

def bin2int(s: str) -> int:
    n = len(s)
    res = 0
    for i in range(n-1, -1, -1):
        res += pow(2, n - 1 - i) * int(s[i])
    return res

# print(int2bin(8))
print(bin2int("1010"))