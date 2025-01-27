class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        l = len(s)
        i = l - 1
        for i in range(l-1, -1, -1):
            if i > 0 and s[i-1] < s[i]:
                break
        if i == 0:
            return -1
        print(s[i-1])
        j = l - 1
        for j in range(l-1, i-1, -1):
            if s[j] > s[i-1]:
                break
        print(s[j])
        s[i-1], s[j] = s[j], s[i-1]
        res = s[:i] + sorted(s[i:])
        return int(''.join(res))



if __name__ == "__main__":
    n = 230241
    print(Solution().nextGreaterElement(n))

