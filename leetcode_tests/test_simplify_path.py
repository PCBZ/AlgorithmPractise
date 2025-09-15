"""
Test suite for LeetCode 71: Simplify Path

This module contains comprehensive test cases for the simplify path problem,
covering various edge cases and path structures.
"""

import unittest
from leetcode.simplify_path import Solution


class TestSimplifyPath(unittest.TestCase):
    """Test cases for Simplify Path solution."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_1(self):
        """Test basic path with trailing slash."""
        path = "/home/"
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/home")

    def test_example_2(self):
        """Test path with parent directory at root."""
        path = "/../"
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/")

    def test_example_3(self):
        """Test path with multiple slashes."""
        path = "/home//foo/"
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/home/foo")

    def test_example_4(self):
        """Test path with current and parent directories."""
        path = "/a/./b/../../c/"
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/c")

    def test_root_only(self):
        """Test root directory."""
        path = "/"
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/")

    def test_multiple_parent_directories(self):
        """Test multiple parent directory references."""
        path = "/a/../../b/../c//.//."
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/c")

    def test_complex_path(self):
        """Test complex path with various components."""
        path = "/a//b////c/d//././/.."
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/a/b/c")

    def test_only_dots(self):
        """Test path with only dots."""
        path = "/./."
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/")

    def test_only_parent_directories(self):
        """Test path with only parent directories."""
        path = "/../.."
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/")

    def test_mixed_valid_names(self):
        """Test path with valid directory names mixed with dots."""
        path = "/home/./Documents/../Downloads/."
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/home/Downloads")

    def test_single_directory(self):
        """Test simple single directory path."""
        path = "/foo"
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/foo")

    def test_nested_directories(self):
        """Test nested directory structure."""
        path = "/a/b/c/d/e"
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/a/b/c/d/e")

    def test_back_to_root(self):
        """Test going back to root from nested path."""
        path = "/a/b/../.."
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/")

    def test_special_directory_names(self):
        """Test directories with special names."""
        path = "/.../"
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/...")

    def test_directory_names_with_dots(self):
        """Test valid directory names that contain dots."""
        path = "/a/.../b/..file/c."
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/a/.../b/..file/c.")

    def test_very_long_path(self):
        """Test handling of longer paths."""
        path = "/a/b/c/d/e/f/g/h/i/j"
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/a/b/c/d/e/f/g/h/i/j")

    def test_alternate_parent_current(self):
        """Test alternating parent and current directory references."""
        path = "/a/../b/./c/../d"
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/b/d")

    def test_trailing_multiple_slashes(self):
        """Test path ending with multiple slashes."""
        path = "/a/b///"
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/a/b")

    def test_leading_multiple_slashes(self):
        """Test path starting with multiple slashes."""
        path = "///a/b"
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/a/b")

    def test_empty_components_throughout(self):
        """Test path with empty components throughout."""
        path = "//a//b//c//"
        result = self.solution.simplifyPath(path)
        self.assertEqual(result, "/a/b/c")


if __name__ == "__main__":
    unittest.main()