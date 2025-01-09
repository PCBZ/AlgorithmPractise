class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def check(left: int, right: int) -> bool:
            length = right - left + 1
            if n % length != 0:
                return False
            c_left, c_right = left + length, right + length 
            while c_right < n:
                for i in range(c_left, c_right + 1):
                    if s[i] != s[left + i - length]:
                        return False
                    print(i, left + i - n)
                c_left += length
                c_right += length
            return True
        
        n = len(s)
        left = 0
        for right in range(n//2):
            if check(left, right):
                return True
        return False 

if __name__ == "__main__":
    s = "aba"
    print(Solution().repeatedSubstringPattern(s))