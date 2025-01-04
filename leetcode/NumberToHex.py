class Solution:
    def toHex(self, num: int) -> str:
        res = ""
        while num:
            digit = num % 16
            digit_str = str(digit) if digit < 10 else chr(digit - 10 + ord('a'))
            res = digit_str + res
            num //= 16
        return res

if __name__ == "__main__":
    print(Solution().toHex(26))