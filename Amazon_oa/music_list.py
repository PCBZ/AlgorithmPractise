class Solution:
    def getMaxAlternatingMusic(self, music: str, k: int) -> int:
        n = len(music)
        pattern1 = ''.join(['0' if i % 2 == 0 else "1" for i in range(n)])
        pattern2 = ''.join(['1' if i % 2 == 1 else "1" for i in range(n)])

        def findPattern(pattern: str) -> int:
            left = 0
            notMatch = 0
            max_len = 0
            for right in range(n):
                if music[right] != pattern[right]:
                    notMatch += 1
                while notMatch > k:
                    if music[left] == pattern[left]:
                        notMatch -= 1
                    left += 1
                max_len = max(max_len, right - left + 1)
            return max_len
        
        return max(findPattern(pattern1), findPattern(pattern2))


if __name__ == "__main__":
    music = "1001"
    k = 1
    print(Solution().getMaxAlternatingMusic(music, k))