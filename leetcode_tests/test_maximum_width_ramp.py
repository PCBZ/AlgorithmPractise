from leetcode.maximum_width_ramp import Solution

def test_examples():
    sol = Solution()
    assert sol.maxWidthRamp([6,0,8,2,1,5]) == 4
    assert sol.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]) == 7
    assert sol.maxWidthRamp([1,2,3,4,5]) == 4
    assert sol.maxWidthRamp([5,4,3,2,1]) == 0
    assert sol.maxWidthRamp([1,1,1,1,1]) == 4
    assert sol.maxWidthRamp([0]) == 0

def test_edge_cases():
    sol = Solution()
    assert sol.maxWidthRamp([]) == 0
    assert sol.maxWidthRamp([1]) == 0
    assert sol.maxWidthRamp([1,0]) == 0
    assert sol.maxWidthRamp([0,1]) == 1
    assert sol.maxWidthRamp([1,2,1,2,1,2]) == 5
    assert sol.maxWidthRamp([10,9,8,7,6,5,4,3,2,1]) == 0
    assert sol.maxWidthRamp([1,2,3,2,1,0,1,2,3,4]) == 9

def test_large_input():
    sol = Solution()
    arr = list(range(10000))
    assert sol.maxWidthRamp(arr) == 9999
    arr = list(reversed(range(10000)))
    assert sol.maxWidthRamp(arr) == 0