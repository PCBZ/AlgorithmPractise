from typing import List

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        def victory(senate: List[str], index: int) -> str:
            if 'R' not in senate:
                return 'Dire'
            if 'D' not in senate:
                return 'Radiant'
            n = len(senate)
            for i in range(index, index + n):
                if senate[index] == 'R' and senate[i % n] == 'D' or (senate[index] == 'D' and senate[i % n] == 'R'):
                    del_index = i % n
                    break
            del senate[del_index]
            next_index = index if del_index < index else (index + 1)
            next_index = next_index % (n - 1)
            return victory(senate, next_index)
        return victory(list(senate), 0)

if __name__ == "__main__":
    senate = "DDRRRR"
    print(Solution().predictPartyVictory(senate))