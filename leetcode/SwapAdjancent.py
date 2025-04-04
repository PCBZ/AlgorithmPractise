class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        n = len(start)
        R_count = L_count = 0
        for i in range(n):
            if R_count > 0:
                if start[i] == 'L' or result[i] == 'L':
                    return False
                if start[i] == 'R':
                    R_count += 1
                if result[i] == 'R':
                    R_count -= 1
            elif L_count > 0:
                if start[i] == 'R' or result[i] == 'R':
                    return False
                if start[i] == 'L':
                    L_count -= 1
                if result[i] == 'L':
                    L_count += 1
            elif start[i] != result[i]:
                if start[i] == 'R' and result[i] == 'X':
                    R_count = 1
                elif start[i] == 'X' and result[i] == 'L':
                    L_count = 1
                else:
                    return False
        if L_count > 0 or R_count > 0:
            return False
        return True
    

if __name__ == "__main__":
    start = "RXXLRXRXL"
    result = "XRLXXRRLX"
    print(Solution().canTransform(start, result))