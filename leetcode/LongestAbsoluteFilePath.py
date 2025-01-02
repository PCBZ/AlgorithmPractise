class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split('\n')
        stack = []
        max_len = 0
        for line in lines:
            depth = line.count('\t')
            name = line.lstrip('\t')

            while len(stack) > depth:
                stack.pop()

            length = len(name) + ( stack[-1] if stack else 0 ) + ( 1 if stack else 0 )
            if '.' in name:
                print(stack, name)
                max_len = max(max_len, length)
            else:
                stack.append(length)
        return max_len


if __name__ == "__main__":
    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(Solution().lengthLongestPath(input))