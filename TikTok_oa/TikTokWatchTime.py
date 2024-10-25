def optimizeTikTokWatchTime(m: int, initialWatch: [int], repeatWatch: [int]) -> int:
    n = len(initialWatch)
    first_round_time = sum([initialWatch[i] + repeatWatch[i] for i in range(n)])
    if m <= n:
        return first_round_time
    sorted_repeated_watch = sorted(repeatWatch)
    repeatWatch_round_time = sum([repeatWatch[i] for i in range(n)])
    rest_times = m - n
    remaining_round = rest_times // n
    remaining_times = rest_times % n
    remaining_watch_times = sum([sorted_repeated_watch[i] for i in range(remaining_times)])

    total_time = first_round_time + remaining_round * repeatWatch_round_time + remaining_watch_times
    return total_time

# Example test case
m = 10
initialWatch = [4, 3, 5]
repeatWatch = [2, 1, 1]

print(optimizeTikTokWatchTime(m, initialWatch, repeatWatch))
