from typing import List

class Solution:
    def pascalTriangle(self, digits: List[int]) -> str:
        while len(digits) > 2:
            next_digits = []
            for i in range(len(digits) - 1):
                next_digits.append((digits[i] + digits[i + 1]) % 10)
            digits = next_digits
        return ''.join(map(str, digits))

if __name__ == "__main__":
    digits = [4, 5, 6, 7]
    print(Solution().pascalTriangle(digits))
