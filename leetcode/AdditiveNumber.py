class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def isValidFrom(first: int, second: int, start: int) -> bool:
            count = 2
            while start < n:
                third = first + second
                third_str = str(third)
                if not num.startswith(third_str, start):
                    return False
                first, second = second, third
                start += len(third_str)
                count += 1
            return count >= 3
        n = len(num)
        for i in range(1, n):
            for j in range(i+1, n+1):
                first, second = num[:i], num[i:j]
                if len(first) > 1 and first[0] == '0' or (len(second) > 1 and second[0] == "0"):
                    continue
                if isValidFrom(int(first), int(second), j):
                    return True
        return False

if __name__ == "__main__":
    num = "112358"
    print(Solution().isAdditiveNumber(num))