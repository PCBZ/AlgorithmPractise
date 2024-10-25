from typing import List

def checkContains(start: int, end: int, disconnectedPairs: List[List[int]]):
    for pair in disconnectedPairs:
        if pair[0] in range(start, end) and pair[1] in range(start, end):
            return False
    return True

def optimizeTikTokRoutes(numServers: int, numDisconnectedPairs: int, disconnectedPairs: List[List[int]]) -> int:
    # total_count = 0
    # for i in range(numServers):
    #     start = i + 1
    #     for j in range(i, numServers):
    #         end = j + 1
    #         # print(start, end)
    #         if not checkContains(start, end, disconnectedPairs):
    #             total_count += 1
    #             print(start, end)
    # return total_count

    disconnected_set = set()
    
    for pair in disconnectedPairs:
        disconnected_set.add((min(pair[0], pair[1]), max(pair[0], pair[1])))
    
    good_subsegment_count = 0
    
    for start in range(1, numServers + 1):
        for end in range(start, numServers + 1):
            is_good = True
            
            # Check pairs in the segment
            for i in range(start, end):
                if (min(i, end), max(i, end)) in disconnected_set:
                    is_good = False
                    break
            
            if is_good:
                print(start, end)
                good_subsegment_count += 1

    return good_subsegment_count


numServers = 4
numDisconnectedPairs = 2
disconnectedPairs = [[1, 2], [2, 3]]

print(optimizeTikTokRoutes(numServers, numDisconnectedPairs, disconnectedPairs))