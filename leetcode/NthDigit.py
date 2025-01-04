class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_count = 1
        range_count = 9
        prev_num = 0
        while n > prev_num + digit_count * range_count:
            prev_num += digit_count * range_count
            digit_count += 1
            range_count *= 10
        
        idx = 10 ** (digit_count - 1) + ( n - prev_num - 1 ) // digit_count
        offset = (n - prev_num - 1) % digit_count
        return int(str(idx)[offset])


if __name__ == "__main__":
    print(Solution().findNthDigit(1000))