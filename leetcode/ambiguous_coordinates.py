from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def get_possibles(t: str) -> List[str]:
            res = []
            if t == format(float(t), "f").rstrip("0").rstrip("."):
                res.append(t)
            for i in range(len(t) - 1):
                n_t = t[:i+1] + "." + t[i+1:]
                if n_t == format(float(n_t), "f").rstrip("0").rstrip("."):
                    res.append(n_t)
            return res
        
        s = s[1:-1]
        res = []
        n = len(s)
        for i in range(n - 1):
            for num1 in get_possibles(s[:i+1]):
                for num2 in get_possibles(s[i+1:]):
                    res.append(f"({num1}, {num2})")

        return res

if __name__ == "__main__":
    s = "(0000001)"
    print(Solution().ambiguousCoordinates(s))
    # s = "(00011)"
    # print(Solution().ambiguousCoordinates(s))
    # s = "(0123)"
    # print(Solution().ambiguousCoordinates(s))
    # s = "(100)"
    # print(Solution().ambiguousCoordinates(s))