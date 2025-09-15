"""
Comprehensive test suite for LeetCode 864: Shortest Path to Get All Keys
"""

import unittest
from leetcode.shortest_path_get_all_keys import Solution


class TestShortestPathAllKeys(unittest.TestCase):
    """Test cases for Shortest Path to Get All Keys problem."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.solution = Solution()
    
    def test_example_1(self):
        """Test basic example with keys and locks."""
        grid = ["@.a.#", "###.#", "b.A.B"]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, 8)
    
    def test_example_2(self):
        """Test multiple paths available."""
        grid = ["@..aA", "..B#.", "....b"]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, 6)
    
    def test_impossible_case(self):
        """Test impossible case - key blocked by its own lock."""
        grid = ["@Aa"]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, -1)
    
    def test_no_keys(self):
        """Test grid with no keys."""
        grid = ["@..."]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, 0)
    
    def test_single_cell_with_start(self):
        """Test single cell grid with only start."""
        grid = ["@"]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, 0)
    
    def test_single_key_adjacent(self):
        """Test single key adjacent to start."""
        grid = ["@a"]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, 1)
    
    def test_multiple_keys_no_locks(self):
        """Test multiple keys without any locks."""
        grid = ["@abc"]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, 3)
    
    def test_complex_maze(self):
        """Test complex maze with multiple keys and locks."""
        grid = [
            "@...a",
            ".###.",
            ".#A#.",
            ".#.#.",
            "...b."
        ]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, 9)
    
    def test_keys_behind_locks(self):
        """Test keys that require other keys to reach."""
        grid = [
            "@.A.",
            "....",
            "a..b"
        ]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, 5)
    
    def test_circular_dependency(self):
        """Test circular dependency case."""
        grid = [
            "@.A.a",
            ".....",
            "b.B.."
        ]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, 8)
    
    def test_all_keys_at_start(self):
        """Test all keys immediately available at start."""
        grid = [
            "abc",
            ".@.",
            "..."
        ]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, 4)
    
    def test_large_grid_performance(self):
        """Test performance with larger grid."""
        grid = [
            "@......",
            ".......",
            ".......",
            ".......",
            ".......",
            "......a"
        ]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, 11)
    
    def test_empty_grid(self):
        """Test empty grid edge case."""
        grid = []
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, -1)
    
    def test_grid_with_empty_row(self):
        """Test grid with empty row."""
        grid = [""]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, -1)
    
    def test_six_keys_maximum(self):
        """Test maximum number of keys (6 keys a-f)."""
        grid = [
            "@abcdef",
            ".......",
            "FEDCBA."
        ]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, 6)
    
    def test_keys_and_locks_mixed(self):
        """Test mixed keys and locks in optimal path."""
        grid = [
            "@..",
            "aA.",
            "b.B"
        ]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, 2)
    
    def test_detour_required(self):
        """Test case requiring detour to collect keys."""
        grid = [
            "@.#.a",
            "..#..",
            "..#..",
            "b...."
        ]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, 10)
    
    def test_blocked_start(self):
        """Test start surrounded by walls except one path."""
        grid = [
            "###",
            "#@.",
            "#.a"
        ]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, 2)
    
    def test_multiple_locks_same_key(self):
        """Test multiple locks for the same key."""
        grid = [
            "@A.A",
            "....",
            "a..."
        ]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, 2)
    
    def test_optimal_path_selection(self):
        """Test that algorithm finds truly optimal path."""
        grid = [
            "@...",
            ".##.",
            ".#a.",
            "b..."
        ]
        result = self.solution.shortestPathAllKeys(grid)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()