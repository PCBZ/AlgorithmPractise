"""
LeetCode 71: Simplify Path

Given a string path representing an absolute path for a Unix-style file system,
return the simplified canonical path.

Rules:
- Single period '.' refers to current directory (ignore)
- Double period '..' refers to parent directory (go back one level)
- Multiple consecutive slashes should be treated as single slash
- Path should start with '/' and not end with '/' (unless root)

URL: https://leetcode.com/problems/simplify-path/
"""


class Solution:  # pylint: disable=too-few-public-methods
    """Solution using stack to process path components."""
    def simplifyPath(self, path: str) -> str:  # pylint: disable=invalid-name
        """
        Simplify Unix-style file system path using stack.

        Time: O(n), Space: O(n)
        """
        stack = []
        components = path.split('/')

        for component in components:
            if component == '..':
                # Go back one directory if possible
                if stack:
                    stack.pop()
            elif component and component != '.':
                # Add valid directory name to path
                stack.append(component)
            # Ignore empty strings and '.' (current directory)

        # Build canonical path
        canonical_path = '/' + '/'.join(stack)
        return canonical_path

if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        "/home/",
        "/../",
        "/home//foo/",
        "/a/./b/../../c/",
        "/a/../../b/../c//.//",
        "/a//b////c/d//././/.."
    ]

    for test_path in test_cases:
        result = solution.simplifyPath(test_path)
        print(f"Input: {test_path!r} -> Output: {result!r}")
