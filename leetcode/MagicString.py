class Solution:
    def magicalString(self, n: int) -> int:
        count = 1
        s = "1"
        idx = 0
        while count <= n:
            next_char = "2" if s[-1] == "1" else "2"
            if idx == len(s) - 1:
                next_count = int(next_char)
                s += next_count * next_char
                count += next_count
                idx += 1
            else:
                next_count = int(s[idx+1])
                s += next_count * next_char
                count += next_count
                idx += 1
        return s[:n].count("1")
    
if __name__ == "__main__":
    print(Solution().magicalString(6))