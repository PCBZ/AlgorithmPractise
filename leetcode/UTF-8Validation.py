from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def countLeadingOnes(num: int) -> int:
            count = 0
            for i in range(7, -1, -1):
                if num >> i & 1 == 1:
                    count += 1
                else:
                    break
            return count
        
        n = len(data)
        start = 0
        while start < n:
            leadingNumber = countLeadingOnes(data[start])
            if leadingNumber == 0:
                start += 1
                continue
            if leadingNumber <= 1 or leadingNumber > 4:
                return False
            if start + leadingNumber > n:
                return False
            for j in range(1, leadingNumber):
                if data[start + j] >> 6 != 0b10:
                    return False
            start += leadingNumber
        return True

if __name__ == "__main__":
    data = [235,140,4]
    print(Solution().validUtf8(data))