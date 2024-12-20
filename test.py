class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for i, ch in enumerate(s):
            if  ch in map1 and map1[ch] != t[i] or ( t[i] in map2 and map2[t[i]] != ch ):
                return False
            map1[ch] = t[i]
            map2[t[i]] = ch
        return True

s = 'badc'
t = 'baba'
print(Solution().isIsomorphic(s, t))