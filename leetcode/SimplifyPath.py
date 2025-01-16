class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        nodes = path.split('/')
        for node in nodes:
            if node == '..' and stack:
                stack.pop()
            if node == '' or node == '.':
                continue
            stack.append(node)
        res = '/'.join(stack)
        res = '/' + res
        return res
    
path = '/home/'
print(Solution().simplifyPath(path))