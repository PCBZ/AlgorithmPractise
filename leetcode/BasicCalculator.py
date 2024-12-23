class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        res = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                num = int(s[start:i])
                res += sign * num
                i -= 1
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif s[i] == ')':
                prev_sign = stack.pop()
                prev_res = stack.pop()
                res = prev_res + prev_sign * res
            
            i += 1
        return res
    
    def calculate2(self, s: str) -> int:
        stack = []
        cur_num = 0
        pre_op = '+'
        for i, char in enumerate(s):
            if char.isdigit():
                cur_num += cur_num * 10 + int(char)
            if char in '+-*/' or i == len(s) - 1:
                if pre_op == '+':
                    stack.append(cur_num)
                elif pre_op == '-':
                    stack.append(-cur_num)
                elif pre_op == '*':
                    stack.append(stack.pop() * cur_num)
                elif pre_op == '/':
                    stack.append(stack.pop() // cur_num)
                pre_op = char
                cur_num = 0
        return sum(stack)
             
            
if __name__ == "__main__":
    s = " 2-1 + 2 "
    print(Solution().calculate(s))
    
    s = "3+2*2"
    print(Solution().calculate2(s))