class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        integer_part = numerator // denominator
        res.append(str(integer_part))
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(res)
        res.append('.')
        remainder_map = {}
        while remainder != 0:
            if remainder in remainder_map:
                idx = remainder_map[remainder]
                res.insert(idx, '(')
                res.append(')')
                break 
            
            remainder_map[remainder] = len(res)
            remainder *= 10
            digit = remainder // denominator
            res.append(str(digit))
            remainder %= denominator
        
        return "".join(res)


if __name__ == "__main__":
    numerator = 4
    denominator = 333
    print(Solution().fractionToDecimal(numerator, denominator))