class Solution:
    def convert(self, s: str, numRows: int) -> str:

        rows = [''] * numRows
        idx = 0
        for ch in s:
            rows[idx] += ch
            if idx == numRows - 1:
                down = False
            if idx == 0:
                down = True
            idx += 1 if down else - 1
        return ''.join(rows)
    
if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert(s, numRows)) # "PAHNAPLSIIGYIR"