def getNonViralCount(video: str, engagementArray: [int]) -> int:
    total_count = 0
    for ch in video:
        if engagementArray[ord(ch) - ord('a')] == 0:
            total_count += 1
    return total_count

def countViralSubstrings(video: str, k: int, engagementArray: [int]) -> int:
    n = len(video)
    total_non_viral = 0
    for start in range(len(video)):
        for end in range(start+1, len(video)+1):
            sub_video = video[start:end]
            if getNonViralCount(sub_video, engagementArray) <= k:
                total_non_viral += 1
    return total_non_viral


video = "stream"
engagementArray = [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k = 2

print(countViralSubstrings(video, k, engagementArray))
# Output = 14
